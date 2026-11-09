---
symbol: "EIF4EBP1"
type: "gene"
col: 11956
ensembl_id: "ENSG00000187840"
name: "eukaryotic translation initiation factor 4E binding protein 1"
location: "8p11.23"
module: 40
arm: "+"
pooled_cpm: 41.47
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# EIF4EBP1

*eukaryotic translation initiation factor 4E binding protein 1* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.55× (z +4.1, q 0.024, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.155× (z -24.0, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPT2]] (+0.76, fdr 7e-06), [[COG5]] (+0.73, fdr 1e-05), [[CSNK2A1]] (+0.72, fdr 1e-05); moves opposite to [[HNRNPH3]] (-0.70, fdr 7e-06), [[BAZ2B]] (-0.70, fdr 3e-05), [[TIA1]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLRC4-KLRK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.024 | 26/47 (SNU-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.024 | 32/48 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.47×** | +3.6 | 0.072 | 28/46 (RPMI-7951, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.48× | +3.3 | 0.13 | 21/44 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.28× | +3.3 | 0.13 | 25/48 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.39× | +3.0 | 0.23 | 23/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.155×** | -24.0 | 0e+00 | 47/47 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.158×** | -16.8 | 0e+00 | 45/47 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.213×** | -13.5 | 2e-39 | 42/47 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.440×** | -10.5 | 1e-23 | 41/47 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.407×** | -8.2 | 4e-14 | 40/48 (HS-578T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.562×** | -7.4 | 2e-11 | 39/48 (J82, KATO III, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.424×** | -7.1 | 1e-10 | 36/48 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.543×** | -5.5 | 2e-06 | 33/48 (KATO III, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.665×** | -5.2 | 1e-05 | 37/48 (A-172, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.574×** | -5.0 | 3e-05 | 31/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -4.4 | 6e-04 | 33/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.601×** | -4.3 | 9e-04 | 33/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -4.3 | 9e-04 | 27/47 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -4.0 | 0.003 | 30/47 (SNU-423, SNU-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.435×** | -3.9 | 0.003 | 34/47 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.646×** | -3.9 | 0.003 | 25/48 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.626×** | -3.9 | 0.003 | 33/48 (C32, SK-MEL-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 44.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -23.7) |
| [[A-172 (line)]] | wt | 96.6 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0653× (z -30.9) |
| [[HS-578T (line)]] | alt | 115 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.0440× (z -33.2) |
| [[H4 (line)]] | wt | 90.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0333× (z -29.9) |
| [[LS 180 (line)]] | wt | 33.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 69.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0669× (z -31.7) |
| [[RKO (line)]] | wt | 34.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.4) |
| [[SNU-423 (line)]] | alt | 38.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -17.8) |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.5) |
| [[HOP62 (line)]] | alt | 64.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0674× (z -24.1) |
| [[J82 (line)]] | alt | 89.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0607× (z -33.6) |
| [[LoVo (line)]] | wt | 23.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -21.8) |
| [[MIA PaCa-2 (line)]] | alt | 50.7 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -12.5) |
| [[PANC-1 (line)]] | alt | 30.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -19.1) |
| [[A498 (line)]] | wt | 50.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0781× (z -23.2) |
| [[CFPAC-1 (line)]] | alt | 88.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0734× (z -24.5) |
| [[NCI-H1792 (line)]] | alt | 37.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 61.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -21.5) |
| [[SW 1088 (line)]] | alt | 65.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0738× (z -11.4) |
| [[SW48 (line)]] | wt | 43.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -13.1) |
| [[SW480 (line)]] | alt | 29.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -20.3) |
| [[A-427 (line)]] | wt | 19.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0738× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -20.7) |
| [[SNU-1 (line)]] | wt | 34.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -12.5) |
| [[A549 (line)]] | wt | 36.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -13.5) |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.3) |
| [[C32 (line)]] | wt | 29.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.9) |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 2 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0487× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 39.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 34.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 63.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.2) |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.9) |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.2) |
| [[HCT15 (line)]] | alt | 42.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -12.1) |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.9) |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -14.6) |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPT2]] | +0.76 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[COG5]] | +0.73 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.72 | +0.78 / +0.51 | both halves | 1e-05 |  |
| [[MPG]] | +0.69 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[TBC1D20]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.68 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[GOT1]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.67 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[MAP2K1]] | +0.67 | +0.69 / +0.54 | both halves | 1e-05 | STRING 418 |
| [[RBAK-RBAKDN]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SESN2]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 | STRING 459 |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH3]] | -0.70 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[BAZ2B]] | -0.70 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[TIA1]] | -0.68 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[CASC9]] | -0.67 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[MED12]] | -0.66 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[DECR1]] | -0.65 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[WAC-AS1]] | -0.64 | -0.64 / -0.24 | both halves | 4e-04 |  |
| [[CACNA2D1]] | -0.63 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[C11orf58]] | -0.63 | -0.66 / -0.30 | both halves | 2e-04 |  |
| [[PATL2]] | -0.62 | -0.64 / -0.28 | both halves | 3e-04 |  |
| [[DDX6]] | -0.61 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[HNRNPH2]] | -0.61 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRC4-KLRK1]] | B | KLRC4-KLRK1 activity lowers EIF4EBP1's level | lines that do not express KLRC4-KLRK1 (29) vs lines expressing it (21) | 1.67× higher at baseline in the lines without KLRC4-KLRK1 | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.6, -19.9); signed map (-44.1, 7.8). **Vector** length 123, 44.0% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.5 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.2 | -3.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.1 | -3.4 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.5 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.9 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.9 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.6 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.2 | -7.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4E binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,030,534-38,060,365 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHAS-I, 4E-BP1 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 6 pathways, smallest: mTORC1-mediated signalling; MTOR signalling; Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13541](https://www.uniprot.org/uniprotkb/Q13541) (Eukaryotic translation initiation factor 4E-binding protein 1):

> Repressor of translation initiation that regulates EIF4E activity by preventing its assembly into the eIF4F complex: hypophosphorylated form competes with EIF4G1/EIF4G3 and strongly binds to EIF4E, leading to repress translation. In contrast, hyperphosphorylated form dissociates from EIF4E, allowing interaction between EIF4G1/EIF4G3 and EIF4E, leading to initiation of translation. Mediates the regulation of protein translation by hormones, growth factors and other stimuli that signal through …

**Summary**, from NCBI Gene [1978](https://www.ncbi.nlm.nih.gov/gene/1978):

> This gene encodes one member of a family of translation repressor proteins. The protein directly interacts with eukaryotic translation initiation factor 4E (eIF4E), which is a limiting component of the multisubunit complex that recruits 40S ribosomal subunits to the 5' end of mRNAs. Interaction of this protein with eIF4E inhibits complex assembly and represses translation. This protein is phosphorylated in response to various signals including UV irradiation and insulin signaling, resulting in …

**Accessions** — [HGNC:3288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3288) · Entrez [1978](https://www.ncbi.nlm.nih.gov/gene/1978) · UniProt [Q13541](https://www.uniprot.org/uniprotkb/Q13541) · Ensembl [ENSG00000187840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187840)

## Data

Gene col 11956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11956); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11956]; `tensor/DDL_lfc|DDL_z.npy` [11956]; `embed/gene_vectors.npy` [11956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11956 or target_col == 11956). Every well: [[EIF4EBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4EBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
