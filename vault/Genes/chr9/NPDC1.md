---
symbol: "NPDC1"
type: "gene"
col: 2840
ensembl_id: "ENSG00000107281"
name: "neural proliferation, differentiation and control 1"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 15.64
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NPDC1

*neural proliferation, differentiation and control 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.91× (z +11.6, q 2e-28, up in 38 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 5.38×, SW480 4.83×, A-172 3.35×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 4.67×, A549 5.24×, HT-29 4.61×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.424× (z -13.2, q 4e-37, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCA2]] (+0.72, fdr 1e-05, ⚠ same locus), [[SH3GLB2]] (+0.68, fdr 2e-05), [[ZDHHC8]] (+0.66, fdr 1e-05), [[TRABD]] (+0.64, fdr 2e-05); moves opposite to [[ZNF764]] (-0.66, fdr 3e-05), [[TRIP11]] (-0.65, fdr 3e-05), [[LZIC]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[JAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2840.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 5.38×, SW480 4.83×, A-172 3.35×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 4.67×, A549 5.24×, HT-29 4.61×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +11.6 | 2e-28 | 38/39 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +10.0 | 3e-21 | 24/25 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.5 | 2e-11 | 29/33 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.53×** | +4.6 | 6e-04 | 24/41 (KATO III, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.1 | 0.004 | 18/40 (MIA PaCa-2, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.76× | +3.2 | 0.12 | 9/30 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | 1.36× | +3.2 | 0.12 | 15/41 (HepG2/C3A, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.424×** | -13.2 | 4e-37 | 40/44 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -8.2 | 9e-14 | 36/43 (SNU-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.639×** | -4.7 | 5e-04 | 23/44 (A-427, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.512×** | -3.8 | 0.019 | 14/42 (SNU-1, CHP-212, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.694×** | -3.7 | 0.023 | 15/45 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.724×** | -3.5 | 0.037 | 16/45 (LoVo, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -3.5 | 0.037 | 18/45 (KATO III, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.707×** | -3.4 | 0.041 | 14/45 (NCI-H2030, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.712×** | -3.4 | 0.048 | 11/45 (NCI-H1573, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 24.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.61× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.0) |
| [[A549 (line)]] | wt | 14.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.4) |
| [[SW480 (line)]] | alt | 9.86 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 50.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.5) |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.9) |
| [[KATO III (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.8) |
| [[LoVo (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.9) |
| [[LS 180 (line)]] | wt | 50.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +10.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 8.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.2) |
| [[RKO (line)]] | wt | 45.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.4) |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -9.3) |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA2]] | +0.72 | +0.77 / +0.53 | both halves | 1e-05 | ⚠ same locus (10.5 kb, same strand: neighbours can correlate without regulation) |
| [[SH3GLB2]] | +0.68 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[ZDHHC8]] | +0.66 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[TRABD]] | +0.64 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[GIT1]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SSBP4]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[KATNB1]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[COL18A1]] | +0.61 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[DHRS1]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[METAP1]] | +0.61 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[INTS11]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF764]] | -0.66 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[TRIP11]] | -0.65 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[LZIC]] | -0.65 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.64 | -0.68 / -0.31 | both halves | 2e-04 |  |
| [[ZNF155]] | -0.62 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[METTL18]] | -0.62 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[C11orf58]] | -0.62 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[BPTF]] | -0.62 | -0.70 / -0.39 | both halves | 5e-05 |  |
| [[LARP7]] | -0.62 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[HELQ]] | -0.61 | -0.70 / -0.31 | both halves | 2e-04 |  |
| [[ZNF140]] | -0.60 | -0.64 / -0.43 | both halves | 4e-05 |  |
| [[LIG4]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | JAG2 activity raises NPDC1's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without JAG2 | 0.064 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[ANKRD13B]] | C | ANKRD13B activity raises NPDC1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.4, -22.9); signed map (-45.3, -9.9). **Vector** length 53.2, 9.08% of its response variance represented; |z| ≥ 3 in 614 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +10.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -13.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -3.8 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | neural proliferation, differentiation and control 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,039,463-137,046,179 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586J0523, CAB-, CAB1 |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQX5](https://www.uniprot.org/uniprotkb/Q9NQX5) (Neural proliferation differentiation and control protein 1):

> Suppresses oncogenic transformation in neural and non-neural cells and down-regulates neural cell proliferation. Might be involved in transcriptional regulation (By similarity).

**Summary**, from NCBI Gene [56654](https://www.ncbi.nlm.nih.gov/gene/56654):

> Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7899) · Entrez [56654](https://www.ncbi.nlm.nih.gov/gene/56654) · UniProt [Q9NQX5](https://www.uniprot.org/uniprotkb/Q9NQX5) · Ensembl [ENSG00000107281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107281)

## Data

Gene col 2840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2840); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2840]; `tensor/DDL_lfc|DDL_z.npy` [2840]; `embed/gene_vectors.npy` [2840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2840 or target_col == 2840). Every well: [[NPDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
