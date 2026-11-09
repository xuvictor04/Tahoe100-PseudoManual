---
symbol: "EMG1"
type: "gene"
col: 4756
ensembl_id: "ENSG00000126749"
name: "EMG1 N1-specific pseudouridine methyltransferase"
location: "12p13.31"
module: 5
arm: "+"
pooled_cpm: 19.23
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 20
n_dd_up_clean: 19
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# EMG1

*EMG1 N1-specific pseudouridine methyltransferase* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.88× (z +11.0, q 3e-25, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.644× (z -7.6, q 1e-11, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC11]] (+0.77, fdr 7e-06), [[ALG8]] (+0.75, fdr 7e-06), [[NIP7]] (+0.73, fdr 7e-06); moves opposite to [[PPP1R2]] (-0.67, fdr 7e-06), [[ARL3]] (-0.67, fdr 7e-06), [[PLEKHH3]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +11.0 | 3e-25 | 38/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +9.7 | 6e-20 | 35/47 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +9.5 | 3e-19 | 38/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +9.1 | 1e-17 | 34/47 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +8.4 | 7e-15 | 35/47 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.57×** | +7.8 | 5e-13 | 24/42 (CFPAC-1, Panc 03.27, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +7.5 | 6e-12 | 30/48 (LOX-IMVI, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.35×** | +7.2 | 3e-11 | 28/47 (NCI-H1792, C32, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.57×** | +7.2 | 3e-11 | 30/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +7.0 | 1e-10 | 28/48 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +7.0 | 2e-10 | 30/47 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.7 | 8e-10 | 25/46 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.5 | 3e-09 | 28/47 (SHP-77, NCI-H2030, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.41×** | +5.8 | 3e-07 | 22/44 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.39×** | +5.8 | 3e-07 | 21/45 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.1 | 1e-05 | 14/48 (HOP62, SW1417, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +4.5 | 2e-04 | 18/44 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.001 | 13/47 (NCI-H2030, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.005 | 7/46 (NCI-H2030, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.006 | 11/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.644×** | -7.6 | 1e-11 | 30/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.445×** | -7.0 | 8e-10 | 30/48 (NCI-H23, CHP-212, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.706×** | -6.0 | 3e-07 | 21/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.712×** | -5.7 | 2e-06 | 22/47 (SW48, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.776×** | -5.4 | 9e-06 | 18/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -5.1 | 3e-05 | 18/48 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.749×** | -5.0 | 5e-05 | 19/48 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.759×** | -4.8 | 1e-04 | 18/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.771×** | -4.5 | 4e-04 | 18/47 (A-427, KATO III, …) | two highest doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.770×** | -4.5 | 5e-04 | 18/48 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.814×** | -4.3 | 0.001 | 15/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.003 | 16/47 (A-427, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.799×** | -3.9 | 0.004 | 16/47 (SW 900, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.791×** | -3.9 | 0.004 | 15/48 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.790×** | -3.8 | 0.004 | 11/47 (SW 1271, A-427, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.859× | -3.6 | 0.011 | 9/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.027 | 11/48 (A-427, NCI-H23, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 8.85 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.109× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 18.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 12.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +12.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 16.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -8.6) |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.118× (z -9.5) |
| [[A-172 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | +0.77 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[ALG8]] | +0.75 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[NIP7]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 958 |
| [[GRWD1]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 | STRING 827 |
| [[DHX37]] | +0.72 | +0.73 / +0.61 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 978 |
| [[METTL1]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 | same gene group |
| [[SNAPC5]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MAK16]] | +0.69 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PIGW]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[E2F3]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TSR1]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 596 |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R2]] | -0.67 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ARL3]] | -0.67 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[PLEKHH3]] | -0.65 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[STK38]] | -0.65 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[GTF2IP4]] | -0.65 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.65 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A23]] | -0.64 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SUFU]] | -0.62 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PPP2R5A]] | -0.62 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[CAT]] | -0.62 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[GNB2]] | -0.61 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EMG1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises EMG1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.6, -33.9); signed map (-0.4, -45.9). **Vector** length 88.9, 18.8% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.58 to 13); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.61 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +7.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | EMG1 N1-specific pseudouridine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,970,913-6,979,936 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C2F, NEP1, Grcc2f |
| Gene groups (HGNC) | SPOUT methyltransferase domain containing; SSU processome; DNA/RNA methyltransferases |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92979](https://www.uniprot.org/uniprotkb/Q92979) (Ribosomal RNA small subunit methyltransferase NEP1):

> S-adenosyl-L-methionine-dependent pseudouridine N(1)-methyltransferase that methylates pseudouridine at position 1248 (Psi1248) in 18S rRNA. Involved the biosynthesis of the hypermodified N1-methyl-N3-(3-amino-3-carboxypropyl) pseudouridine (m1acp3-Psi) conserved in eukaryotic 18S rRNA. Is not able to methylate uridine at this position. Also has an essential role in 40S ribosomal subunit biogenesis independent on its methyltransferase activity, facilitating the incorporation of ribosomal …

**Summary**, from NCBI Gene [10436](https://www.ncbi.nlm.nih.gov/gene/10436):

> This gene encodes an essential, conserved eukaryotic protein that methylates pseudouridine in 18S rRNA. The related protein in yeast is a component of the small subunit processome and is essential for biogenesis of the ribosomal 40S subunit. A mutation in this gene has been associated with Bowen-Conradi syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:16912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16912) · Entrez [10436](https://www.ncbi.nlm.nih.gov/gene/10436) · UniProt [Q92979](https://www.uniprot.org/uniprotkb/Q92979) · Ensembl [ENSG00000126749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126749)

## Data

Gene col 4756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4756); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4756]; `tensor/DDL_lfc|DDL_z.npy` [4756]; `embed/gene_vectors.npy` [4756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4756 or target_col == 4756). Every well: [[EMG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
