---
symbol: "ST20-MTHFS"
type: "gene"
col: 15186
ensembl_id: "ENSG00000259332"
name: "ST20-MTHFS readthrough"
location: "15q25.1"
module: 23
arm: "+"
pooled_cpm: 27.0
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ST20-MTHFS

*ST20-MTHFS readthrough* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.65× (z +8.0, q 1e-12, up in 32 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.52× (z +6.9, q 2e-09, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.585× (z -8.8, q 7e-16, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R3F]] (+0.69, fdr 1e-05), [[MIRLET7IHG]] (+0.66, fdr 1e-05), [[TEX22]] (+0.63, fdr 1e-05); moves opposite to [[EFNA4]] (-0.53, fdr 1e-04), [[CERS6]] (-0.52, fdr 3e-05), [[MCU]] (-0.52, fdr 9e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRDX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +8.0 | 1e-12 | 32/43 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.9 | 2e-09 | 26/46 (LoVo, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.7 | 4e-04 | 18/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.6 | 5e-04 | 18/46 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +4.4 | 0.001 | 17/48 (HEC-1-A, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.006 | 17/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.070 | 7/48 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.23×** | +3.3 | 0.071 | 8/47 (SK-MEL-2, A549, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.085 | 11/47 (A-172, A498, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.085 | 11/48 (RKO, LS 180, …) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.13 | 6/45 (H4, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15186.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.585×** | -8.8 | 7e-16 | 38/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.628×** | -7.6 | 6e-12 | 29/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.651×** | -7.0 | 3e-10 | 29/48 (A-427, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -7.0 | 3e-10 | 29/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.675×** | -6.4 | 1e-08 | 27/48 (A-427, A549, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.713×** | -5.6 | 3e-06 | 24/48 (A-427, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -5.4 | 5e-06 | 25/48 (A549, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.553×** | -5.1 | 3e-05 | 24/45 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.768×** | -4.3 | 9e-04 | 21/47 (BT-474, PANC-1, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.654×** | -3.6 | 0.015 | 10/37 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.797×** | -3.4 | 0.030 | 13/47 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.065 | 6/48 (C-33 A, SW 1088, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.817×** | -3.2 | 0.065 | 8/48 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.773× | -3.0 | 0.11 | 7/48 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 71.6 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -20.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 34.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 50.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.0610× (z -10.6) |
| [[A549 (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[C32 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0799× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 24.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.132× (z -9.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -13.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0863× (z -9.0) |
| [[SW1417 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.12× (z +9.3) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R3F]] | +0.69 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MIRLET7IHG]] | +0.66 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TEX22]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.63 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[RFX3-DT]] | +0.61 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ST7L]] | +0.61 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[SMIM15-AS1]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[HAVCR2]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.61 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[CDKL3]] | +0.60 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[C19orf18]] | +0.60 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TAS2R4]] | +0.60 | +0.55 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA4]] | -0.53 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[CERS6]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[MCU]] | -0.52 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[UQCRC1]] ⚠ | -0.52 | -0.39 / -0.42 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EFNA3]] | -0.51 | -0.48 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDX2]] | B | PRDX2 activity lowers ST20-MTHFS's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.72× higher at baseline in the lines without PRDX2 | 0.057 | ⚠ within organs, on part of the lines; also absent: RAB20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (27.2, -11.8); signed map (17.3, 1.1). **Vector** length 97.0, 21.2% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.4 | -7.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.2 | -6.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.6 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -8.8 |
|  | [[NG25 (drug)]] 5 µM |  | -4.3 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -7.0 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.4 | -3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ST20-MTHFS readthrough |
| Locus type | readthrough (other) |
| Location | 15q25.1 — chr15:79,845,150-79,923,754 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100528021](https://www.ncbi.nlm.nih.gov/gene/100528021):

> This locus represents naturally occurring read-through transcription between the neighboring suppressor of tumorigenicity 20 and 5,10-methenyltetrahydrofolate synthetase (5-formyltetrahydrofolate cyclo-ligase) genes on chromosome 15. The read-through transcript produces a fusion protein that shares sequence identity with each individual gene product. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:44655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44655) · Entrez [100528021](https://www.ncbi.nlm.nih.gov/gene/100528021) · Ensembl [ENSG00000259332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259332)

## Data

Gene col 15186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15186); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15186]; `tensor/DDL_lfc|DDL_z.npy` [15186]; `embed/gene_vectors.npy` [15186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15186 or target_col == 15186). Every well: [[ST20-MTHFS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST20-MTHFS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
