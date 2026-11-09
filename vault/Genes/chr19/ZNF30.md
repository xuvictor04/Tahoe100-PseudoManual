---
symbol: "ZNF30"
type: "gene"
col: 9680
ensembl_id: "ENSG00000168661"
name: "zinc finger protein 30"
location: "19q13.13"
module: 17
arm: "+"
pooled_cpm: 4.09
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZNF30

*zinc finger protein 30* — 19q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.27× (z +17.1, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.676× (z -4.6, q 0.002, down in 14 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF74]] (+0.66, fdr 1e-05), [[TM7SF3]] (+0.64, fdr 1e-05), [[FXN]] (+0.64, fdr 2e-05); moves opposite to [[ALOX12-AS1]] (-0.65, fdr 2e-04), [[CCNT2-AS1]] (-0.63, fdr 1e-04), [[ATXN1L]] (-0.59, fdr 3e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[POTEF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.27×** | +17.1 | 0e+00 | 43/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.18×** | +16.9 | 0e+00 | 40/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.58×** | +15.0 | 0e+00 | 39/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.99×** | +12.4 | 3e-33 | 19/23 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.40×** | +10.3 | 5e-23 | 36/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +7.9 | 2e-13 | 26/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.93×** | +7.7 | 9e-13 | 19/35 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.91×** | +7.6 | 1e-12 | 22/45 (A549, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +7.1 | 7e-11 | 14/35 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +5.9 | 2e-07 | 10/45 (A549, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +5.8 | 3e-07 | 14/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.53×** | +5.7 | 5e-07 | 10/41 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +5.7 | 5e-07 | 11/45 (PANC-1, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.6 | 1e-06 | 11/34 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +4.8 | 5e-05 | 8/41 (PANC-1, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 2e-04 | 11/41 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -4.6 | 0.002 | 14/42 (SW480, SHP-77, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -4.5 | 0.002 | 18/45 (LoVo, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -3.4 | 0.083 | 16/32 (HOP62, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.749×** | -3.4 | 0.083 | 19/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.751×** | -3.4 | 0.083 | 9/42 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.764× | -3.2 | 0.12 | 7/44 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.756× | -3.2 | 0.12 | 7/37 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.828× | -3.1 | 0.12 | 19/38 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.85 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.07× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0662× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -9.9) |
| [[HOP62 (line)]] | alt | 3.64 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0792× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Saquinavir (drug)]] 5 µM 0.182× (z -9.5) |
| [[C-33 A (line)]] | alt | 8.20 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0520× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 7.34 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 4.60 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0715× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 5.68 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -9.7) |
| [[SW1417 (line)]] | alt | 5.81 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -9.9) |
| [[SW480 (line)]] | alt | 7.11 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.91× (z +8.8) | — |
| [[A-172 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF74]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 | same gene group |
| [[TM7SF3]] | +0.64 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[FXN]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[KBTBD6]] | +0.64 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.64 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SUGT1P4-STRA6LP]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[FITM2]] | +0.63 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[METTL5]] | +0.62 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[SLC25A12]] | +0.62 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[CHST10]] | +0.61 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[NDUFA12]] | +0.61 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TRIM35]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALOX12-AS1]] | -0.65 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[CCNT2-AS1]] | -0.63 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ATXN1L]] | -0.59 | -0.28 / -0.63 | both halves | 3e-04 |  |
| [[TTC41P]] | -0.58 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[FBXL19-AS1]] | -0.57 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[HCG17]] | -0.56 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[CCDC90B-AS1]] | -0.56 | -0.13 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[RBM15-AS1]] | -0.56 | -0.22 / -0.46 | both halves | 6e-04 |  |
| [[SLC25A53]] | -0.55 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[IL18BP]] | -0.55 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[PPP1R15B-AS1]] | -0.55 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[EOLA2-DT]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[FTX]] | -0.54 | -0.31 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POTEF]] | B | POTEF activity raises ZNF30's level | lines that do not express POTEF (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without POTEF | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.7, -3.7); signed map (-24.4, -15.0). **Vector** length 63.7, 9.56% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +7.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.13 — chr19:34,926,903-34,945,170 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX28, DKFZp686N19164, FLJ20562 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Reactome | 3 pathways, smallest: Regulation of endogenous retroelements by KRAB-ZFP proteins; Regulation of endogenous retroelements; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P17039](https://www.uniprot.org/uniprotkb/P17039) (Zinc finger protein 30):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [90075](https://www.ncbi.nlm.nih.gov/gene/90075):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13090) · Entrez [90075](https://www.ncbi.nlm.nih.gov/gene/90075) · UniProt [P17039](https://www.uniprot.org/uniprotkb/P17039) · Ensembl [ENSG00000168661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168661)

## Data

Gene col 9680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9680); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9680]; `tensor/DDL_lfc|DDL_z.npy` [9680]; `embed/gene_vectors.npy` [9680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9680 or target_col == 9680). Every well: [[ZNF30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
