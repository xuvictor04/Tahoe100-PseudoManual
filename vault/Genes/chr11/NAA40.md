---
symbol: "NAA40"
type: "gene"
col: 3148
ensembl_id: "ENSG00000110583"
name: "N-alpha-acetyltransferase 40, NatD catalytic subunit"
location: "11q13.1"
module: 26
arm: "-"
pooled_cpm: 12.68
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# NAA40

*N-alpha-acetyltransferase 40, NatD catalytic subunit* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.60× (z +15.6, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.435× (z -19.2, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD17]] (+0.69, fdr 1e-05), [[WRAP73]] (+0.65, fdr 3e-05), [[SLC39A3]] (+0.65, fdr 3e-05); moves opposite to [[CPEB2-DT]] (-0.71, fdr 1e-05), [[CCT6B]] (-0.68, fdr 3e-05), [[SEPTIN7-DT]] (-0.66, fdr 3e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.60×** | +15.6 | 0e+00 | 43/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +14.6 | 0e+00 | 39/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +14.5 | 3e-45 | 41/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +9.3 | 2e-18 | 14/21 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +8.5 | 2e-15 | 31/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.1 | 5e-14 | 23/38 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +6.8 | 9e-10 | 23/47 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +6.4 | 1e-08 | 14/29 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.49×** | +6.3 | 2e-08 | 24/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.8 | 1e-04 | 14/48 (BT-474, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +4.6 | 2e-04 | 12/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.004 | 14/47 (AsPC-1, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.4 | 0.028 | 16/48 (LS 180, NCI-H2347, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.039 | 4/48 (PANC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.22×** | +3.3 | 0.041 | 10/41 (BT-474, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[DT-061 (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.094 | 2/42 (HCT15, LOX-IMVI) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.435×** | -19.2 | 0e+00 | 41/46 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.610×** | -11.4 | 1e-27 | 34/46 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -6.8 | 2e-09 | 24/44 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -6.4 | 2e-08 | 24/46 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -5.8 | 9e-07 | 20/45 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -4.4 | 0.001 | 14/43 (A-427, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.038 | 13/47 (NCI-H460, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **0.796×** | -3.4 | 0.040 | 17/45 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.701× | -3.0 | 0.15 | 9/47 (J82, AN3 CA, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 26.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.0753× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 8.96 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.1) |
| [[PANC-1 (line)]] | alt | 17.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.5) |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0916× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.2) |
| [[C32 (line)]] | wt | 10.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -11.5) |
| [[COLO 205 (line)]] | alt | 7.51 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.5) |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -9.6) |
| [[J82 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 10.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -8.7) |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 7.48 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.7) |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0982× (z -8.8) |
| [[SW 900 (line)]] | alt | 9.21 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.140× (z -8.6) |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -8.9) |
| [[SW480 (line)]] | alt | 16.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +9.3) | — |
| [[A-172 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*14 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD17]] | +0.69 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.65 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[SLC39A3]] | +0.65 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[ZNF445]] | +0.64 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[RRP1B]] | +0.63 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PAFAH1B3]] | +0.63 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[CASP2]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[COMMD2]] | +0.61 | +0.27 / +0.60 | both halves | 3e-04 |  |
| [[PTGES2]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[GGA1]] | +0.59 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[GPRIN1]] | +0.58 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[SLC23A2]] | +0.58 | +0.52 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*86 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPEB2-DT]] | -0.71 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CCT6B]] | -0.68 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[SEPTIN7-DT]] | -0.66 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[DENND6A-AS1]] | -0.66 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MALINC1]] | -0.66 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[FAM184B]] | -0.66 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ACTR3-AS1]] | -0.66 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | -0.66 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SPATA1]] | -0.66 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | -0.65 | -0.54 / -0.29 | both halves | 3e-04 |  |
| [[SIAH2-AS1]] | -0.65 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CCDC181]] | -0.65 | -0.62 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers NAA40's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.61× higher at baseline in the lines without ZNF341-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises NAA40's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.2, 14.0); signed map (-27.1, -15.3). **Vector** length 80.6, 14.8% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.6 | +14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +15.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +14.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.1 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.0 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.9 | -19.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 40, NatD catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:63,938,959-63,957,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13848; previously NAT11 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UY6](https://www.uniprot.org/uniprotkb/Q86UY6) (N-alpha-acetyltransferase 40):

> N-alpha-acetyltransferase that specifically mediates the acetylation of the N-terminal residues of histones H4 and H2A. In contrast to other N-alpha-acetyltransferase, has a very specific selectivity for histones H4 and H2A N-terminus and specifically recognizes the 'Ser-Gly-Arg-Gly sequence'. Acts as a negative regulator of apoptosis. May play a role in hepatic lipid metabolism (By similarity).

**Summary**, from NCBI Gene [79829](https://www.ncbi.nlm.nih.gov/gene/79829):

> Enables histone H2A acetyltransferase activity; histone H4 acetyltransferase activity; and protein N-terminal-serine acetyltransferase activity. Predicted to be involved in chromatin remodeling. Predicted to act upstream of or within lipid metabolic process. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25845) · Entrez [79829](https://www.ncbi.nlm.nih.gov/gene/79829) · UniProt [Q86UY6](https://www.uniprot.org/uniprotkb/Q86UY6) · Ensembl [ENSG00000110583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110583)

## Data

Gene col 3148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3148); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3148]; `tensor/DDL_lfc|DDL_z.npy` [3148]; `embed/gene_vectors.npy` [3148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3148 or target_col == 3148). Every well: [[NAA40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
