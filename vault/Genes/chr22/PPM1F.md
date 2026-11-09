---
symbol: "PPM1F"
type: "gene"
col: 1850
ensembl_id: "ENSG00000100034"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1F"
location: "22q11.22"
module: 2
arm: "+"
pooled_cpm: 19.66
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PPM1F

*protein phosphatase, Mg2+/Mn2+ dependent 1F* — 22q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.91× (z +12.9, q 1e-35, up in 21 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.24× (z +4.4, q 0.001, up in 10 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.451× (z -23.3, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW2]] (+0.73, fdr 1e-05), [[ERCC2]] (+0.72, fdr 7e-06), [[ANKS6]] (+0.70, fdr 7e-06); moves opposite to [[TCEAL1]] (-0.63, fdr 6e-05), [[HHLA3]] (-0.63, fdr 3e-05), [[PIGP]] (-0.63, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[H2AJ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +12.9 | 1e-35 | 21/28 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +12.9 | 2e-35 | 29/40 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.47×** | +8.1 | 1e-13 | 29/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.41×** | +7.1 | 2e-10 | 26/48 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.43×** | +6.9 | 5e-10 | 16/35 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +4.4 | 0.001 | 10/48 (NCI-H1792, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.22×** | +4.1 | 0.003 | 17/48 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.004 | 7/45 (HCT15, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.008 | 2/43 (RPMI-7951, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | 1.13× | +3.5 | 0.022 | 5/48 (KATO III, NCI-H1573, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.4 | 0.030 | 5/33 (A498, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | 1.18× | +3.3 | 0.053 | 18/44 (MIA PaCa-2, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.451×** | -23.3 | 0e+00 | 41/47 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.443×** | -16.2 | 0e+00 | 38/47 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.556×** | -12.1 | 1e-31 | 28/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -9.3 | 2e-18 | 28/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.801×** | -6.5 | 1e-08 | 22/47 (PANC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.578×** | -5.9 | 3e-07 | 23/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.813×** | -5.3 | 1e-05 | 17/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.795×** | -4.6 | 2e-04 | 14/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.793×** | -4.6 | 3e-04 | 15/47 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.801×** | -4.4 | 6e-04 | 16/45 (LoVo, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.816×** | -4.2 | 0.001 | 19/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.820×** | -4.1 | 0.002 | 6/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.697×** | -3.9 | 0.004 | 15/46 (A-427, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -3.9 | 0.004 | 11/48 (HS-578T, AN3 CA, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.851× | -3.8 | 0.005 | 11/48 (Hs 766T, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.705×** | -3.8 | 0.005 | 18/46 (C32, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.829×** | -3.7 | 0.006 | 12/47 (HEC-1-A, LOX-IMVI, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.850× | -3.6 | 0.010 | 10/48 (SW48, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 31.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.6) |
| [[PANC-1 (line)]] | alt | 22.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.7) |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.5) |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.8) |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.5) |
| [[Hs 766T (line)]] | wt | 60.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.4) |
| [[J82 (line)]] | alt | 15.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.226× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 23.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.179× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 33.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -16.7) |
| [[RKO (line)]] | wt | 31.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.0) |
| [[SW480 (line)]] | alt | 18.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.8) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -13.2) |
| [[A549 (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.3) |
| [[COLO 205 (line)]] | alt | 7.48 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0803× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.267× (z -9.9) |
| [[HS-578T (line)]] | alt | 28.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.461× (z -9.0) |
| [[LoVo (line)]] | wt | 15.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -8.8) |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.7) |
| [[SW48 (line)]] | wt | 24.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.169× (z -9.6) |
| [[A-172 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ERCC2]] | +0.72 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TBC1D24]] | +0.69 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[AP3M2]] | +0.69 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[PACC1]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.68 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[POLRMT]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[NCLN]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ATP13A2]] | +0.65 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TRABD]] | +0.65 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ATAD3A]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEAL1]] | -0.63 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[HHLA3]] | -0.63 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[PIGP]] | -0.63 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[LGALS3]] | -0.62 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.62 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[C11orf71]] | -0.60 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[ABCA5]] | -0.60 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[AHI1-DT]] | -0.59 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[PNRC1]] | -0.59 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.59 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[H2AJ]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | -0.59 | -0.56 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[H2AJ]] | B | H2AJ activity lowers PPM1F's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.37× higher at baseline in the lines without H2AJ | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[HDAC6]] | B | HDAC6 activity lowers PPM1F's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.0, -26.0); signed map (-42.4, -9.9). **Vector** length 85.9, 16.7% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.1 | +8.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.9 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | +7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +0.2 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.4 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -23.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -12.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.22 — chr22:21,919,425-21,952,848 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FEM-2, KIAA0015, POPX2, CaMKPase, CAMKP |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Reactome | 5 pathways, smallest: Negative regulation of NMDA receptor-mediated neuronal transmission; Activation of NMDA receptors and postsynaptic events; Neurotransmitter receptors and postsynaptic signal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [P49593](https://www.uniprot.org/uniprotkb/P49593) (Protein phosphatase 1F):

> Dephosphorylates and concomitantly deactivates CaM-kinase II activated upon autophosphorylation, and CaM-kinases IV and I activated upon phosphorylation by CaM-kinase kinase. Promotes apoptosis.

**Summary**, from NCBI Gene [9647](https://www.ncbi.nlm.nih.gov/gene/9647):

> The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase can interact with Rho guanine nucleotide exchange factors (PIX), and thus block the effects of p21-activated kinase 1 (PAK), a protein kinase mediating biological effects downstream of Rho GTPases. Calcium/calmodulin-dependent protein kinase II gamma (CAMK2G/CAMK-II) is found to be one of the …

**Accessions** — [HGNC:19388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19388) · Entrez [9647](https://www.ncbi.nlm.nih.gov/gene/9647) · UniProt [P49593](https://www.uniprot.org/uniprotkb/P49593) · Ensembl [ENSG00000100034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100034)

## Data

Gene col 1850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1850); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1850]; `tensor/DDL_lfc|DDL_z.npy` [1850]; `embed/gene_vectors.npy` [1850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1850 or target_col == 1850). Every well: [[PPM1F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
