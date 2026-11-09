---
symbol: "TTC32"
type: "gene"
col: 11471
ensembl_id: "ENSG00000183891"
name: "tetratricopeptide repeat domain 32"
location: "2p24.1"
module: 23
arm: "+"
pooled_cpm: 9.18
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# TTC32

*tetratricopeptide repeat domain 32* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +11.8, q 1e-29, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.641× (z -6.1, q 7e-07, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTY2D1OS]] (+0.73, fdr 6e-05), [[PBLD]] (+0.72, fdr 2e-04), [[MR1]] (+0.72, fdr 4e-05); moves opposite to [[SH3PXD2B]] (-0.67, fdr 1e-04), [[ANKRD27]] (-0.65, fdr 4e-04), [[STUB1]] (-0.65, fdr 0.004, ⚠ not reproduced), [[ST6GALNAC4]] (-0.65, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +11.8 | 1e-29 | 35/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +10.5 | 3e-23 | 27/37 (NCI-H1573, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +9.9 | 7e-21 | 19/27 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +8.3 | 1e-14 | 24/44 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.1 | 1e-10 | 17/30 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +6.5 | 8e-09 | 19/47 (A498, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.9 | 3e-07 | 21/41 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.8 | 6e-07 | 7/18 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.4 | 3e-06 | 8/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +4.9 | 5e-05 | 17/45 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.008 | 12/48 (A-172, PANC-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.008 | 12/48 (HEC-1-A, SW 1271, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.6 | 0.017 | 7/39 (MIA PaCa-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trimetrexate (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.043 | 5/46 (HT-29, SK-MEL-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.047 | 3/47 (J82, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.641×** | -6.1 | 7e-07 | 20/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -5.7 | 4e-06 | 21/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.697×** | -4.9 | 1e-04 | 15/47 (NCI-H661, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.720×** | -4.5 | 0.001 | 15/47 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -3.6 | 0.040 | 12/45 (KATO III, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -3.4 | 0.056 | 12/48 (H4, SHP-77, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.796× | -3.1 | 0.14 | 16/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.649× | -3.1 | 0.14 | 5/46 (KATO III, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.62 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +16.0) | [[Neratinib (drug)]] 0.05 µM 0.102× (z -12.8) |
| [[A498 (line)]] | wt | 8.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.112× (z -9.4) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0754× (z -10.5) |
| [[Hs 766T (line)]] | wt | 9.90 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0923× (z -10.6) |
| [[KATO III (line)]] | alt | 15.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.149× (z -9.7) |
| [[LS 180 (line)]] | wt | 7.10 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0647× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 9.66 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0590× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 7.51 | 0 | 1 | — | [[SBI-0640756 (drug)]] 5 µM 0.0497× (z -9.7) |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTY2D1OS]] | +0.73 | +0.73 / +0.39 | both halves | 6e-05 |  |
| [[PBLD]] | +0.72 | +0.63 / +0.31 | both halves | 2e-04 |  |
| [[MR1]] | +0.72 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[KMT2E-AS1]] | +0.72 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[OXA1L-DT]] | +0.71 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[AHI1-DT]] | +0.71 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[PPP1R3F]] | +0.71 | +0.71 / +0.32 | both halves | 2e-04 |  |
| [[TMEM202-AS1]] | +0.71 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[GALNT7-DT]] | +0.71 | +0.67 / +0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[HEXIM2-AS1]] | +0.70 | +0.66 / +0.31 | both halves | 2e-04 |  |
| [[C11orf71]] | +0.70 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | +0.69 | +0.70 / +0.37 | both halves | 7e-05 |  |
| [[EMSY-DT]] | +0.69 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.67 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.65 | -0.62 / -0.24 | both halves | 4e-04 |  |
| [[STUB1]] | -0.65 | -0.46 / -0.07 | ⚠ not reproduced | 0.004 | same gene group |
| [[ST6GALNAC4]] | -0.65 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[FLNB]] | -0.64 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[EHD4]] | -0.64 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[SPTLC2]] | -0.64 | -0.65 / -0.23 | both halves | 5e-04 |  |
| [[RNF216P1]] | -0.62 | -0.66 / -0.33 | both halves | 1e-04 |  |
| [[GNAI2]] | -0.62 | -0.50 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[TWF2]] | -0.62 | -0.56 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[YIF1B]] | -0.62 | -0.61 / +0.10 | ⚠ one half (not replicated) | 1.00 |  |
| [[WASF3]] | -0.61 | -0.56 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TTC32's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises TTC32's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises TTC32's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[STAT5A]] | B | STAT5A activity lowers TTC32's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.48× higher at baseline in the lines without STAT5A | 0.084 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (2.0, 16.9); signed map (24.6, -13.5). **Vector** length 71.4, 11.6% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +10.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.5 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:19,896,631-19,901,983 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q5I0X7](https://www.uniprot.org/uniprotkb/Q5I0X7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32954) · Entrez [130502](https://www.ncbi.nlm.nih.gov/gene/130502) · UniProt [Q5I0X7](https://www.uniprot.org/uniprotkb/Q5I0X7) · Ensembl [ENSG00000183891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183891)

## Data

Gene col 11471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11471); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11471]; `tensor/DDL_lfc|DDL_z.npy` [11471]; `embed/gene_vectors.npy` [11471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11471 or target_col == 11471). Every well: [[TTC32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
