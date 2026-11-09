---
symbol: "RABEPK"
type: "gene"
col: 5941
ensembl_id: "ENSG00000136933"
name: "Rab9 effector protein with kelch motifs"
location: "9q33.3"
module: 33
arm: "+"
pooled_cpm: 23.22
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RABEPK

*Rab9 effector protein with kelch motifs* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +9.6, q 3e-19, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.456× (z -17.9, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EARS2]] (+0.75, fdr 7e-06), [[GPR89A]] (+0.75, fdr 7e-06), [[IQCB1]] (+0.72, fdr 7e-06); moves opposite to [[TMEM14C]] (-0.63, fdr 1e-05), [[VEZF1]] (-0.60, fdr 1e-05), [[FMR1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.6 | 3e-19 | 32/48 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.79×** | +9.4 | 2e-18 | 37/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.76×** | +8.8 | 4e-16 | 34/45 (SW 900, NCI-H460, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.93×** | +5.5 | 4e-06 | 29/47 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.89×** | +5.4 | 1e-05 | 21/47 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 1e-05 | 26/48 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.83×** | +5.1 | 3e-05 | 22/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.37×** | +5.0 | 4e-05 | 22/48 (HT-29, KATO III, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 4e-05 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.51×** | +4.7 | 1e-04 | 16/48 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +4.6 | 2e-04 | 18/48 (MIA PaCa-2, J82, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.32×** | +4.5 | 3e-04 | 23/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +4.5 | 4e-04 | 20/48 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.001 | 15/46 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.60×** | +4.0 | 0.003 | 15/40 (NCI-H1573, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.003 | 14/46 (A549, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.034 | 8/47 (SHP-77, A-172, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.054 | 7/48 (J82, A549, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.060 | 8/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.096 | 3/48 (NCI-H460, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Everolimus (drug)]] 5 µM |  | **1.27×** | +2.8 | 0.096 | 3/48 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.456×** | -17.9 | 0e+00 | 42/47 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.502×** | -11.1 | 3e-26 | 36/48 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -8.2 | 5e-14 | 31/47 (MIA PaCa-2, A498, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -6.4 | 2e-08 | 25/47 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.544×** | -5.1 | 3e-05 | 26/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.734×** | -5.0 | 6e-05 | 23/47 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.775×** | -4.1 | 0.003 | 18/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.008 | 14/47 (HOP62, CHP-212, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.081 | 15/48 (SW480, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.821×** | -3.2 | 0.081 | 19/48 (HOP62, LS 180, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | 0.819× | -3.1 | 0.10 | 11/48 (LoVo, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 24.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.1) |
| [[A498 (line)]] | wt | 49.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -19.4) |
| [[A-172 (line)]] | wt | 39.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.4) |
| [[SW480 (line)]] | alt | 30.1 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.37× (z +9.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.4) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -13.8) |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 25.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.4) |
| [[KATO III (line)]] | alt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.2) |
| [[LoVo (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.165× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 30.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -14.1) |
| [[A549 (line)]] | wt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.2) |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.9) |
| [[H4 (line)]] | wt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -13.1) |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0706× (z -11.8) |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.3) |
| [[J82 (line)]] | alt | 21.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.2) |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.5) |
| [[PANC-1 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.7) |
| [[RKO (line)]] | wt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.2) |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EARS2]] | +0.75 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[GPR89A]] | +0.75 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[IQCB1]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 | STRING 444 |
| [[SLC30A6]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[TRIM27]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SRM]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[PDCD11]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PAM16]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[FAM86DP]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[DEXI]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[GEMIN5]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[DCUN1D5]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM14C]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[FMR1]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[PLXNB2]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPH2]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ATP7A]] | -0.56 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SYNE2]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CCDC50]] | -0.55 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[BAZ2B]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[AHR]] | -0.54 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[OTUD1]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises RABEPK's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without NT5M | 0.019 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.0, -18.1); signed map (-43.0, -19.3). **Vector** length 107, 25.7% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +5.4 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.2 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.5 | +5.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.5 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +4.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -17.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.3 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.8 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | Rab9 effector protein with kelch motifs |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:125,200,542-125,234,161 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAB9P40, bA65N13.1 |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6M1](https://www.uniprot.org/uniprotkb/Q7Z6M1) (Rab9 effector protein with kelch motifs):

> Rab9 effector required for endosome to trans-Golgi network (TGN) transport.

**Summary**, from NCBI Gene [10244](https://www.ncbi.nlm.nih.gov/gene/10244):

> Predicted to be involved in receptor-mediated endocytosis and vesicle docking involved in exocytosis. Predicted to be located in cytoplasmic vesicle; cytosol; and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16896) · Entrez [10244](https://www.ncbi.nlm.nih.gov/gene/10244) · UniProt [Q7Z6M1](https://www.uniprot.org/uniprotkb/Q7Z6M1) · Ensembl [ENSG00000136933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136933)

## Data

Gene col 5941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5941); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5941]; `tensor/DDL_lfc|DDL_z.npy` [5941]; `embed/gene_vectors.npy` [5941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5941 or target_col == 5941). Every well: [[RABEPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABEPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
