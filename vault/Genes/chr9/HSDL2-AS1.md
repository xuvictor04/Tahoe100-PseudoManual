---
symbol: "HSDL2-AS1"
type: "gene"
col: 13739
ensembl_id: "ENSG00000230185"
name: "HSDL2 antisense RNA 1"
location: "9q32"
module: 35
arm: "+"
pooled_cpm: 9.81
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 11
n_dd_up_clean: 23
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# HSDL2-AS1

*HSDL2 antisense RNA 1* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.40× (z +26.1, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.623× (z -7.1, q 6e-10, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALINC1]] (+0.74, fdr 1e-05), [[PSMD14-DT]] (+0.72, fdr 1e-05), [[INTS6-AS1]] (+0.71, fdr 7e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +26.1 | 0e+00 | 43/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +12.4 | 1e-32 | 35/48 (J82, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +11.0 | 5e-26 | 32/45 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.1 | 2e-17 | 28/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.9 | 4e-17 | 30/45 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.8 | 6e-13 | 21/37 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.3 | 3e-11 | 19/44 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +7.2 | 6e-11 | 24/48 (SHP-77, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +7.0 | 2e-10 | 25/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +6.9 | 2e-10 | 27/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +6.8 | 6e-10 | 13/24 (J82, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +6.2 | 3e-08 | 20/47 (LoVo, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.1 | 5e-08 | 9/15 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +6.0 | 1e-07 | 18/46 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.6 | 1e-06 | 17/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +5.1 | 2e-05 | 13/47 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +5.0 | 2e-05 | 17/46 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 6e-04 | 13/47 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -7.1 | 6e-10 | 28/47 (PANC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -6.8 | 4e-09 | 21/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -6.4 | 3e-08 | 22/45 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.688×** | -5.6 | 3e-06 | 16/46 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -5.6 | 3e-06 | 21/47 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -5.1 | 4e-05 | 20/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.721×** | -4.9 | 7e-05 | 13/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -4.5 | 4e-04 | 13/39 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -3.6 | 0.020 | 11/47 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.793×** | -3.5 | 0.027 | 7/48 (PANC-1, NCI-H661, …) | all doses, flat | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.647×** | -3.4 | 0.031 | 9/43 (SK-MEL-2, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 16.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.41× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.101× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 16.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +14.5) | — |
| [[J82 (line)]] | alt | 10.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 12.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.8) | [[Cobimetinib (drug)]] 0.05 µM 0.166× (z -9.0) |
| [[SW480 (line)]] | alt | 11.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +14.5) | — |
| [[A-172 (line)]] | wt | 6.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +11.1) | — |
| [[A498 (line)]] | wt | 6.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +11.7) | — |
| [[A549 (line)]] | wt | 8.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 8.10 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.101× (z -8.7) |
| [[HOP62 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 8.24 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0964× (z -10.2) |
| [[HS-578T (line)]] | alt | 5.68 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0886× (z -8.8) |
| [[HT-29 (line)]] | alt | 5.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +10.8) | — |
| [[LoVo (line)]] | wt | 8.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 8.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 5.69 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.144× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +13.2) | — |
| [[RKO (line)]] | wt | 9.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 8.83 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0692× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.192× (z -9.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 6.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +11.3) | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALINC1]] | +0.74 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[PSMD14-DT]] | +0.72 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | +0.71 | +0.76 / +0.37 | both halves | 7e-05 | same gene group |
| [[PAXBP1-AS1]] | +0.71 | +0.75 / +0.52 | both halves | 1e-05 | same gene group |
| [[TMEM202-AS1]] | +0.71 | +0.77 / +0.39 | both halves | 6e-05 | same gene group |
| [[LRP2BP]] | +0.70 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[PSMD7-DT]] | +0.70 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[LRRC8C-DT]] | +0.70 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[SPESP1]] | +0.69 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[DENND6A-AS1]] | +0.69 | +0.72 / +0.45 | both halves | 3e-05 | same gene group |
| [[MFF-DT]] | +0.69 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[SPEN-AS1]] | +0.68 | +0.68 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HSDL2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.9, 22.2); signed map (29.5, -1.6). **Vector** length 61.1, 9.15% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +26.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +9.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.1 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | +6.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | HSDL2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q32 — chr9:112,399,512-112,487,204 (-) |
| Ensembl biotype | lncRNA |
| Also known as | bA32M23.3; previously C9orf147 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31438) · Entrez [100133204](https://www.ncbi.nlm.nih.gov/gene/100133204) · Ensembl [ENSG00000230185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230185)

## Data

Gene col 13739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13739); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13739]; `tensor/DDL_lfc|DDL_z.npy` [13739]; `embed/gene_vectors.npy` [13739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13739 or target_col == 13739). Every well: [[HSDL2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSDL2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
