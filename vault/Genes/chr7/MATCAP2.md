---
symbol: "MATCAP2"
type: "gene"
col: 8960
ensembl_id: "ENSG00000164542"
name: "microtubule associated tyrosine carboxypeptidase 2"
location: "7p14.2"
module: 36
arm: "-"
pooled_cpm: 29.67
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# MATCAP2

*microtubule associated tyrosine carboxypeptidase 2* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +11.7, q 1e-28, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.688× (z -6.4, q 7e-08, down in 24 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-423 0.164×, Panc 03.27 0.222×, LoVo 0.335×, MIA PaCa-2 0.317×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.277×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0871×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.235×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX16]] (+0.60, fdr 1e-05), [[KPNA5]] (+0.57, fdr 1e-05), [[HLA-V-1]] (+0.55, fdr 3e-05); moves opposite to [[GBA2]] (-0.59, fdr 1e-05), [[TRAPPC10]] (-0.58, fdr 1e-05), [[ZMYND19]] (-0.56, fdr 3e-05).
> It sits in the **-** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +11.7 | 1e-28 | 36/46 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +7.7 | 5e-12 | 25/46 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.9 | 7e-10 | 23/46 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +6.5 | 1e-08 | 25/46 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.30×** | +6.3 | 3e-08 | 23/46 (LoVo, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +6.2 | 5e-08 | 24/46 (A-427, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 1e-04 | 25/45 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +4.8 | 1e-04 | 17/46 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +4.3 | 0.001 | 16/46 (C32, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.002 | 18/46 (LoVo, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 17/45 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +3.8 | 0.006 | 10/46 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.016 | 10/46 (C32, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.018 | 9/46 (MIA PaCa-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.019 | 13/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.034 | 11/46 (SW1417, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.037 | 8/45 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.041 | 8/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.068 | 11/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8960.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-423 0.164×, Panc 03.27 0.222×, LoVo 0.335×, MIA PaCa-2 0.317×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.277×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0871×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.235×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.688×** | -6.4 | 7e-08 | 24/39 (SNU-423, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.784×** | -4.0 | 0.015 | 18/45 (SW480, NCI-H23, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.861× | -3.7 | 0.047 | 10/46 (SW480, HCT15, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.694× | -3.3 | 0.12 | 9/35 (NCI-H460, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[DTP3 (drug)]] 5 µM |  | 0.695× | -3.3 | 0.12 | 9/43 (HS-578T, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.878× | -3.2 | 0.14 | 15/46 (BT-474, A-172, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.19 | 8/46 (SW 1088, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 78.7 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LoVo (line)]] | wt | 44.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[PANC-1 (line)]] | alt | 62.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.53× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 67.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[A-427 (line)]] | wt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.05× (z +11.0) | — |
| [[A498 (line)]] | wt | 33.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.0) | — |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.120× (z -9.2) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 34.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 36.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.235× (z -9.3) |
| [[HT-29 (line)]] | alt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[RKO (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -11.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0871× (z -11.3) |
| [[SNU-423 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX16]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[KPNA5]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[HLA-V-1]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[BTN2A2]] | +0.53 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[HSBP1L1]] | +0.52 | +0.61 / +0.28 | both halves | 3e-04 |  |
| [[RPS6KA6]] | +0.52 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[BTN2A3P]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[NKIRAS1]] | +0.50 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[MINDY1]] | +0.50 | +0.46 / +0.37 | both halves | 8e-05 |  |
| [[OTUD6B-AS1]] | +0.50 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[ZNF711]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[TTC33]] | +0.50 | +0.51 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBA2]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TRAPPC10]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ZMYND19]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ARPC5L]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[PYCR3]] | -0.55 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[MICAL2]] | -0.55 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[FBH1]] | -0.55 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[IL9RP3]] | -0.53 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[PGP]] | -0.53 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[PDCD6]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[PITPNC1]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[E2F4]] | -0.51 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MATCAP2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **-** arm (projection on the module's main direction -0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (15.3, -8.2); signed map (17.6, -14.3). **Vector** length 73.9, 13.7% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.6 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +6.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.0 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +3.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.7 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated tyrosine carboxypeptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2 — chr7:36,324,152-36,390,125 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TMCP2; previously KIAA0895 |
| Gene groups (HGNC) | Microtubule associated tyrosine carboxypeptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCT3](https://www.uniprot.org/uniprotkb/Q8NCT3) (Putative tyrosine carboxypeptidase MATCAP2):

> Putative tyrosine carboxypeptidase.

**Summary**, from NCBI Gene [23366](https://www.ncbi.nlm.nih.gov/gene/23366):

> Predicted to enable carboxypeptidase activity; metal ion binding activity; and metallopeptidase activity. Predicted to be involved in proteolysis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22206) · Entrez [23366](https://www.ncbi.nlm.nih.gov/gene/23366) · UniProt [Q8NCT3](https://www.uniprot.org/uniprotkb/Q8NCT3) · Ensembl [ENSG00000164542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164542)

## Data

Gene col 8960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8960); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8960]; `tensor/DDL_lfc|DDL_z.npy` [8960]; `embed/gene_vectors.npy` [8960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8960 or target_col == 8960). Every well: [[MATCAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MATCAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
