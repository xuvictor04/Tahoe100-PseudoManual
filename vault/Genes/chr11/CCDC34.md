---
symbol: "CCDC34"
type: "gene"
col: 3090
ensembl_id: "ENSG00000109881"
name: "coiled-coil domain containing 34"
location: "11p14.1"
module: 67
arm: "+"
pooled_cpm: 36.89
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CCDC34

*coiled-coil domain containing 34* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.43× (z +8.9, q 2e-16, up in 35 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.56× (z +3.2, q 0.068, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 5.80×, A-172 4.62×, KATO III 5.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 5.81×; ⚠ cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 7.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.536× (z -4.7, q 0.002, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTF2]] (+0.70, fdr 1e-05), [[CTDSPL2]] (+0.67, fdr 1e-05), [[CENPC]] (+0.62, fdr 1e-05); moves opposite to [[RNF32-AS1]] (-0.50, fdr 2e-04), [[USP45]] (-0.50, fdr 3e-04), [[LTO1]] (-0.49, fdr 4e-04).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MRPS25]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3090.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 5.80×, A-172 4.62×, KATO III 5.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 5.81×; ⚠ cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 7.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **3.43×** | +8.9 | 2e-16 | 35/38 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **4.02×** | +8.3 | 2e-14 | 43/43 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **2.16×** | +5.4 | 1e-05 | 36/42 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **2.00×** | +5.2 | 2e-05 | 42/45 (HT-29, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.51×** | +4.4 | 0.001 | 40/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.73×** | +4.1 | 0.003 | 34/48 (A498, HT-29, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.61×** | +3.6 | 0.028 | 28/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.61×** | +3.5 | 0.035 | 30/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.57×** | +3.4 | 0.041 | 26/48 (PANC-1, HepG2/C3A, …) | two highest doses | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.068 | 30/47 (HS-578T, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | 1.52× | +3.0 | 0.12 | 21/43 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -4.7 | 0.002 | 38/48 (NCI-H23, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.582×** | -4.1 | 0.014 | 29/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -3.9 | 0.015 | 26/48 (SNU-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.603×** | -3.8 | 0.020 | 30/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.394×** | -3.7 | 0.028 | 32/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.623×** | -3.3 | 0.096 | 29/48 (LS 180, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 59.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.81× (z +10.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[KATO III (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0729× (z -10.9) |
| [[A-427 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 51.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTF2]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[CTDSPL2]] | +0.67 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CENPC]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SASS6]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[HAUS4]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MNS1]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HPF1]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RPA3]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PEX3]] | +0.58 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SMC2]] | +0.58 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ATP5IF1]] | +0.58 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[MIS18BP1]] | +0.56 | +0.38 / +0.55 | both halves | 7e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF32-AS1]] | -0.50 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[USP45]] | -0.50 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[LTO1]] | -0.49 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[ZNF800]] | -0.49 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[DESI1]] | -0.48 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[DPH5-DT]] | -0.48 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[ZPR1]] | -0.48 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[PRMT3]] | -0.48 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[PUS1]] | -0.48 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[PEA15]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[UNC50]] | -0.47 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ZNF121]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CCDC34's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRPS25]] | C | CCDC34's natural level strengthens MRPS25's drug response | CCDC34's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.37; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.8, -51.8); signed map (-44.8, -36.5). **Vector** length 71.3, 22.4% of its response variance represented; |z| ≥ 3 in 693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | +0.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.7 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.1 — chr11:27,330,827-27,363,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-41, L15, RAMA3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HJ3](https://www.uniprot.org/uniprotkb/Q96HJ3) (Coiled-coil domain-containing protein 34):

> Involved in spermatogenesis. Has a probable role in anterograde intraflagellar transport which is essential for the formation of sperm flagella.

**Summary**, from NCBI Gene [91057](https://www.ncbi.nlm.nih.gov/gene/91057):

> Involved in spermatogenesis. Located in sperm flagellum and sperm head-tail coupling apparatus. Implicated in spermatogenic failure 76. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25079) · Entrez [91057](https://www.ncbi.nlm.nih.gov/gene/91057) · UniProt [Q96HJ3](https://www.uniprot.org/uniprotkb/Q96HJ3) · Ensembl [ENSG00000109881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109881)

## Data

Gene col 3090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3090); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3090]; `tensor/DDL_lfc|DDL_z.npy` [3090]; `embed/gene_vectors.npy` [3090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3090 or target_col == 3090). Every well: [[CCDC34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
