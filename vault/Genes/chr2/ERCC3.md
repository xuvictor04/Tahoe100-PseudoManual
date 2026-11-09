---
symbol: "ERCC3"
type: "gene"
col: 8647
ensembl_id: "ENSG00000163161"
name: "ERCC excision repair 3, TFIIH core complex helicase subunit"
location: "2q14.3"
module: 36
arm: "+"
pooled_cpm: 42.56
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ERCC3

*ERCC excision repair 3, TFIIH core complex helicase subunit* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.37× (z +8.4, q 2e-14, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.716× (z -12.7, q 3e-34, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.611× (z -12.4, q 8e-33, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C3]] (+0.65, fdr 7e-06), [[ZNF384]] (+0.64, fdr 7e-06), [[SH3BP5L]] (+0.64, fdr 7e-06); moves opposite to [[QKI]] (-0.58, fdr 1e-05), [[CGGBP1]] (-0.56, fdr 2e-05), [[SLC50A1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +8.4 | 2e-14 | 31/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.23×** | +8.0 | 5e-13 | 24/48 (Hs 766T, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.34×** | +7.4 | 2e-11 | 32/48 (HOP62, SW480, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.8 | 1e-06 | 22/43 (RKO, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +5.0 | 7e-05 | 20/48 (HOP62, HT-29, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.42×** | +4.9 | 7e-05 | 11/47 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.21×** | +4.9 | 7e-05 | 17/47 (LS 180, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +4.8 | 1e-04 | 19/49 (SW480, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.14× | +3.5 | 0.025 | 5/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.4 | 0.044 | 6/35 (HT-29, A549, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.3 | 0.046 | 1/48 (HT-29) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.12× | +3.1 | 0.089 | 6/48 (CFPAC-1, SW48, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8647.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.716×** | -12.7 | 3e-34 | 31/48 (C32, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.611×** | -12.4 | 8e-33 | 42/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.696×** | -9.8 | 3e-20 | 32/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -7.9 | 4e-13 | 2/49 (SW48, SW 1088) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.766×** | -6.7 | 3e-09 | 25/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.788×** | -6.4 | 1e-08 | 23/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -6.2 | 5e-08 | 21/48 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | **0.809×** | -5.3 | 9e-06 | 20/44 (SNU-1, PANC-1, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -5.2 | 1e-05 | 20/48 (HEC-1-A, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.829×** | -5.0 | 3e-05 | 19/47 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -4.2 | 0.001 | 19/48 (A-427, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.872× | -3.7 | 0.010 | 10/49 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.872× | -3.7 | 0.010 | 17/48 (NCI-H460, SW 1271, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.872× | -3.7 | 0.010 | 17/48 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.883× | -3.3 | 0.031 | 6/48 (BT-474, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.0 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.422× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.438× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 51.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -18.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.304× (z -11.6) |
| [[PANC-1 (line)]] | alt | 42.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.473× (z -9.1) |
| [[A-172 (line)]] | wt | 41.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.395× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 29.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 56.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[A-427 (line)]] | wt | 47.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 41.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.440× (z -8.6) |
| [[AN3 CA (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[C-33 A (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -16.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -15.1) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[NCI-H23 (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C3]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ZNF384]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SH3BP5L]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SAMM50]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[NUP214]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 | pathway: HIV Infection |
| [[ZNF875]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[METTL16]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HIV Infection |
| [[HERC2P3]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[INTS4]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[DHX57]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QKI]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.56 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[SLC50A1]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TMEM14C]] | -0.54 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[UBR5]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[SGO1-AS1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PDLIM3]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PTBP3]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[BMAL1]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[BCL3]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers ERCC3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-30.5, -9.4); signed map (-33.8, -27.6). **Vector** length 92.9, 19.2% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.8 | +8.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | +7.4 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.1 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +5.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.2 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -12.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.4 | -12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.8 | -6.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 3, TFIIH core complex helicase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,257,290-127,294,166 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XPB, BTF2, RAD25, Ssl2 |
| Gene groups (HGNC) | Xeroderma pigmentosum complementation groups; ERCC excision repair associated; General transcription factor IIH complex subunits; DexD/H helicases |
| Hallmark sets | PEROXISOME, DNA_REPAIR |
| Reactome | 42 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [P19447](https://www.uniprot.org/uniprotkb/P19447) (General transcription and DNA repair factor IIH helicase/translocase subunit XPB):

> ATP-dependent 3'-5' DNA helicase/translocase. Binds dsDNA rather than ssDNA, unzipping it in a translocase rather than classical helicase activity. Component of the general transcription and DNA repair factor IIH (TFIIH) core complex. When complexed to CDK-activating kinase (CAK), involved in RNA transcription by RNA polymerase II. The ATPase activity of XPB/ERCC3, but not its helicase activity, is required for DNA opening; it may wrap around the damaged DNA wedging it open, causing localized …

**Summary**, from NCBI Gene [2071](https://www.ncbi.nlm.nih.gov/gene/2071):

> This gene encodes an ATP-dependent DNA helicase that functions in nucleotide excision repair. The encoded protein is a subunit of basal transcription factor 2 (TFIIH) and, therefore, also functions in class II transcription. Mutations in this gene are associated with Xeroderma pigmentosum B, Cockayne's syndrome, and trichothiodystrophy. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:3435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3435) · Entrez [2071](https://www.ncbi.nlm.nih.gov/gene/2071) · UniProt [P19447](https://www.uniprot.org/uniprotkb/P19447) · Ensembl [ENSG00000163161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163161)

## Data

Gene col 8647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8647); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8647]; `tensor/DDL_lfc|DDL_z.npy` [8647]; `embed/gene_vectors.npy` [8647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8647 or target_col == 8647). Every well: [[ERCC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
