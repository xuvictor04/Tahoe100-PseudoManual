---
symbol: "N6AMT1"
type: "gene"
col: 7961
ensembl_id: "ENSG00000156239"
name: "HemK methyltransferase 2, ETF1 glutamine and histone H4 lysine"
location: "21q21.3"
module: 1
arm: "+"
pooled_cpm: 4.13
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# N6AMT1

*HemK methyltransferase 2, ETF1 glutamine and histone H4 lysine* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +9.4, q 3e-18, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.62× (z +5.5, q 4e-06, up in 16 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.538× (z -10.0, q 5e-21, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM185B]] (+0.73, fdr 7e-06), [[FKTN]] (+0.72, fdr 7e-06), [[COA7]] (+0.72, fdr 7e-06); moves opposite to [[KDELR1]] (-0.71, fdr 7e-06), [[NARF]] (-0.63, fdr 1e-05), [[TPTEP2-CSNK1E]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAR2P1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +9.4 | 3e-18 | 4/7 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +5.6 | 4e-06 | 6/10 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +5.5 | 4e-06 | 16/45 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +5.5 | 4e-06 | 9/44 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +5.5 | 4e-06 | 10/47 (NCI-H460, C-33 A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.1 | 4e-05 | 5/23 (LOX-IMVI, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +5.0 | 4e-05 | 12/44 (A-172, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 1e-04 | 14/38 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.7 | 2e-04 | 8/20 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.7 | 0.011 | 2/48 (NCI-H1792, HT-29) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.011 | 9/44 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.011 | 7/45 (C32, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.020 | 10/45 (A549, NCI-H1573, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.039 | 7/34 (CFPAC-1, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -10.0 | 5e-21 | 29/38 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -7.0 | 9e-10 | 20/34 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -5.7 | 2e-06 | 16/39 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -5.6 | 3e-06 | 19/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -4.7 | 3e-04 | 14/32 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -4.5 | 7e-04 | 14/45 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -3.4 | 0.060 | 8/44 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.744×** | -3.2 | 0.082 | 7/36 (RKO, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.764× | -3.1 | 0.13 | 13/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.49 | 0 | 2 (2 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0607× (z -10.2) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 5.14 | 0 | 2 (1 ⚠) | — | [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.0658× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 3.46 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.0797× (z -8.5) |
| [[PANC-1 (line)]] | alt | 5.69 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -8.6) |
| [[SW480 (line)]] | alt | 7.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[FKTN]] | +0.72 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[COA7]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[HUS1]] | +0.70 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[C5orf63]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[PTCD2]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SAYSD1]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[C12orf29]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PIGO]] | +0.69 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[IMPACT]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RRP15]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MGA]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR1]] | -0.71 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[NARF]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.63 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.63 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[OST4]] | -0.62 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.61 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[PMS2P4-1]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.61 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[EMSY]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[UBL5]] | -0.60 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[TESK2]] | -0.59 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TNXB]] | -0.59 | -0.41 / -0.61 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAR2P1]] | B | FAR2P1 activity raises N6AMT1's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without FAR2P1 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[TOP2A]] | B | TOP2A activity raises N6AMT1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.7, 1.1); signed map (0.6, -38.3). **Vector** length 53.1, 6.40% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.9 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -0.9 | -0.3 |
|  | [[Rifaximin (drug)]] 0.5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | HemK methyltransferase 2, ETF1 glutamine and histone H4 lysine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:28,872,191-28,885,371 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRED28, N6AMT, MTQ2, KMT9, PrmC; previously N6AMT1, C21orf127 |
| Gene groups (HGNC) | Glutamine methyltransferases; 7BS protein glutamine methyltransferases |
| Reactome | 5 pathways, smallest: Methylation; Phase II - Conjugation of compounds; Eukaryotic Translation Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5N5](https://www.uniprot.org/uniprotkb/Q9Y5N5) (Methyltransferase HEMK2):

> Methyltransferase that can methylate proteins and, to a lower extent, arsenic. Catalytic subunit of a heterodimer with TRMT112, which monomethylates 'Lys-12' of histone H4 (H4K12me1), a modification present at the promoters of numerous genes encoding cell cycle regulators. Catalytic subunit of a heterodimer with TRMT112, which catalyzes N5-methylation of Glu residue of proteins with a Gly-Gln-Xaa-Xaa-Xaa-Arg motif. Methylates ETF1 on 'Gln-185'; ETF1 needs to be complexed to ERF3 in its …

**Summary**, from NCBI Gene [29104](https://www.ncbi.nlm.nih.gov/gene/29104):

> This gene encodes an N(6)-adenine-specific DNA methyltransferase. The encoded enzyme may be involved in the methylation of release factor I during translation termination. This enzyme is also involved in converting the arsenic metabolite monomethylarsonous acid to the less toxic dimethylarsonic acid. Alternative splicing of this gene results in multiple transcript variants. A related pseudogene has been identified on chromosome 11. [provided by RefSeq, Mar 2023]

**Accessions** — [HGNC:16021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16021) · Entrez [29104](https://www.ncbi.nlm.nih.gov/gene/29104) · UniProt [Q9Y5N5](https://www.uniprot.org/uniprotkb/Q9Y5N5) · Ensembl [ENSG00000156239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156239)

## Data

Gene col 7961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7961); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7961]; `tensor/DDL_lfc|DDL_z.npy` [7961]; `embed/gene_vectors.npy` [7961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7961 or target_col == 7961). Every well: [[N6AMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/N6AMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
