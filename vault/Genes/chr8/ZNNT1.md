---
symbol: "ZNNT1"
type: "gene"
col: 15323
ensembl_id: "ENSG00000261087"
name: "ZNF706 neighboring transcript 1"
location: "8q22.3"
module: 37
arm: "+"
pooled_cpm: 5.27
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# ZNNT1

*ZNF706 neighboring transcript 1* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.79× (z +12.4, q 8e-33, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Retinoic acid (drug)]] 0.05 µM: 0.617× (z -4.2, q 0.018, down in 15 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 0.5 µM in 1 line (A-172 0.0469×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 0.107×; ⚠ toxic; transcription drop); [[Cepharanthine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0907×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF706]] (+0.79, fdr 7e-06, ⚠ read-through risk), [[PIWIL2]] (+0.73, fdr 7e-06), [[KLRD1]] (+0.70, fdr 7e-06), [[UPP2]] (+0.70, fdr 7e-06); moves opposite to [[DROSHA]] (-0.59, fdr 1e-05), [[NCBP1]] (-0.59, fdr 1e-05), [[NUP155]] (-0.59, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02609]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +12.4 | 8e-33 | 35/40 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +10.2 | 5e-22 | 34/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +8.9 | 8e-17 | 31/39 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.80×** | +8.8 | 1e-16 | 38/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.1 | 1e-10 | 26/37 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.25×** | +7.0 | 3e-10 | 29/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +6.9 | 3e-10 | 23/31 (J82, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +6.7 | 1e-09 | 18/27 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.15×** | +6.6 | 3e-09 | 31/43 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.03×** | +6.1 | 6e-08 | 28/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.0 | 1e-07 | 24/46 (HS-578T, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +4.9 | 4e-05 | 18/46 (NCI-H460, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +4.8 | 6e-05 | 20/41 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.73×** | +4.7 | 1e-04 | 23/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.7 | 1e-04 | 14/40 (SW1417, HOP62, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.65×** | +4.1 | 0.001 | 14/45 (A498, J82, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.004 | 15/45 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.006 | 15/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.51×** | +3.5 | 0.013 | 14/46 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15323.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 0.5 µM in 1 line (A-172 0.0469×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 0.107×; ⚠ toxic; transcription drop); [[Cepharanthine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0907×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.617×** | -4.2 | 0.018 | 15/46 (Hs 766T, KATO III, …) | inconsistent across doses | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | 0.672× | -3.4 | 0.14 | 16/45 (COLO 205, Hs 766T, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.676× | -3.4 | 0.14 | 14/46 (A549, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.686× | -3.1 | 0.22 | 16/42 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.698× | -3.1 | 0.22 | 7/47 (C32, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.60 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +12.3) | — |
| [[A-172 (line)]] | wt | 6.22 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.0469× (z -11.2) |
| [[A498 (line)]] | wt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.3) | — |
| [[C32 (line)]] | wt | 5.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 8.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 9.40 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 9.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 5.56 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0907× (z -9.2) |
| [[SW480 (line)]] | alt | 4.99 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.47× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF706]] | +0.79 | +0.73 / +0.79 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 8.2 kb 3′ of ZNF706 on the same strand (can correlate by spillover, not regulation) |
| [[PIWIL2]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[KLRD1]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[UPP2]] | +0.70 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[SNX31]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[EIF1]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CASS4]] | +0.67 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CD247]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[THAP3]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LINC00640]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[BET1]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DROSHA]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[NCBP1]] | -0.59 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[NUP155]] | -0.59 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[PDHA1]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[LAS1L]] | -0.58 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[API5]] | -0.58 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.57 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[DNM1L]] | -0.57 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PHB1]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DLAT]] | -0.56 | -0.49 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02609]] | B | LINC02609 activity lowers ZNNT1's level | lines that do not express LINC02609 (6) vs lines expressing it (44) | 1.30× higher at baseline in the lines without LINC02609 | 0.094 | ⚠ within organs, on part of the lines; also absent: TPST1, HLTF, FERMT2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, -17.1); signed map (11.5, 4.1). **Vector** length 74.9, 13.7% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +0.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +1.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -3.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ZNF706 neighboring transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q22.3 — chr8:101,166,805-101,169,629 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AP003469.4 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54438) · Entrez [115830329](https://www.ncbi.nlm.nih.gov/gene/115830329) · Ensembl [ENSG00000261087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261087)

## Data

Gene col 15323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15323); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15323]; `tensor/DDL_lfc|DDL_z.npy` [15323]; `embed/gene_vectors.npy` [15323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15323 or target_col == 15323). Every well: [[ZNNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
