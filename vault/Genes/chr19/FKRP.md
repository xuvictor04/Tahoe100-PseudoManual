---
symbol: "FKRP"
type: "gene"
col: 11159
ensembl_id: "ENSG00000181027"
name: "fukutin related protein"
location: "19q13.32"
module: 88
arm: "+"
pooled_cpm: 8.12
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# FKRP

*fukutin related protein* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +20.8, q 0e+00, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.663× (z -6.2, q 4e-07, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP3CB-AS1]] (+0.79, fdr 1e-05), [[RAB30-DT]] (+0.75, fdr 1e-05), [[ST7L]] (+0.74, fdr 1e-05); moves opposite to [[GMCL1]] (-0.76, fdr 1e-05), [[MMS19]] (-0.70, fdr 7e-06), [[SHQ1]] (-0.70, fdr 4e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +20.8 | 0e+00 | 40/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +11.4 | 2e-27 | 33/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +11.1 | 2e-26 | 8/19 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +10.6 | 4e-24 | 27/32 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +8.1 | 8e-14 | 15/23 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +6.8 | 8e-10 | 23/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.0 | 2e-07 | 15/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.0 | 4e-05 | 3/48 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.8 | 1e-04 | 17/47 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 5e-04 | 12/47 (C32, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.007 | 10/46 (LoVo, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.014 | 11/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.017 | 5/48 (PANC-1, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.5 | 0.017 | 8/40 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.030 | 8/47 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.049 | 6/47 (SW480, H4, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.056 | 2/45 (BT-474, KATO III) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.080 | 4/47 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.083 | 3/46 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.098 | 1/48 (KATO III) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -6.2 | 4e-07 | 22/47 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.713×** | -5.1 | 1e-04 | 19/47 (KATO III, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.719×** | -5.0 | 1e-04 | 17/47 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.566×** | -4.5 | 0.001 | 12/47 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.815×** | -4.3 | 0.002 | 10/48 (NCI-H1573, CHP-212, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.792×** | -3.5 | 0.044 | 14/47 (RKO, C-33 A, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.646×** | -3.4 | 0.049 | 10/43 (A-427, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.80 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +12.8) | — |
| [[A-172 (line)]] | wt | 5.61 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0874× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 6.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 8.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 9.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +8.6) | — |
| [[LoVo (line)]] | wt | 7.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 7.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 6.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.5) | — |
| [[SK-MEL-2 (line)]] | alt | 9.60 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 9.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | +0.79 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.75 | +0.80 / +0.49 | both halves | 1e-05 |  |
| [[ST7L]] | +0.74 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.74 | +0.78 / +0.35 | both halves | 1e-04 |  |
| [[FIZ1]] | +0.73 | +0.77 / +0.34 | both halves | 1e-04 |  |
| [[ZNF655]] | +0.72 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[BRPF3]] | +0.72 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[MEPCE]] | +0.71 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[SLC9A8]] | +0.71 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | +0.71 | +0.81 / +0.39 | both halves | 6e-05 |  |
| [[AFG3L1P]] | +0.70 | +0.75 / +0.43 | both halves | 3e-05 |  |
| [[AKT1S1]] | +0.70 | +0.70 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.76 | -0.79 / -0.56 | both halves | 1e-05 |  |
| [[MMS19]] | -0.70 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[SHQ1]] | -0.70 | -0.73 / -0.41 | both halves | 4e-05 |  |
| [[RELCH]] | -0.69 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[BAG4]] | -0.69 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.68 | -0.71 / -0.36 | both halves | 9e-05 |  |
| [[MOSPD3]] | -0.68 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.68 | -0.70 / -0.37 | both halves | 9e-05 |  |
| [[HDAC3]] | -0.68 | -0.73 / -0.47 | both halves | 2e-05 |  |
| [[SDHAP1]] | -0.68 | -0.75 / -0.43 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.67 | -0.73 / -0.43 | both halves | 3e-05 |  |
| [[CNOT8]] | -0.67 | -0.71 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FKRP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-8.1, 5.4); signed map (18.3, -25.1). **Vector** length 72.3, 11.4% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +20.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.8 | -6.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.6 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | fukutin related protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,746,046-46,776,988 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LGMD2I, MDC1C, FKTR |
| Reactome | 3 pathways, smallest: Matriglycan biosynthesis on DAG1; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9S5](https://www.uniprot.org/uniprotkb/Q9H9S5) (Ribitol 5-phosphate transferase FKRP):

> Catalyzes the transfer of a ribitol 5-phosphate from CDP-L-ribitol to the ribitol 5-phosphate previously attached by FKTN/fukutin to the phosphorylated O-mannosyl trisaccharide (N-acetylgalactosamine-beta-3-N-acetylglucosamine-beta-4-(phosphate-6-)mannose), a carbohydrate structure present in alpha-dystroglycan (DAG1). This constitutes the second step in the formation of the ribose 5-phosphate tandem repeat which links the phosphorylated O-mannosyl trisaccharide to the ligand binding moiety …

**Summary**, from NCBI Gene [79147](https://www.ncbi.nlm.nih.gov/gene/79147):

> This gene encodes a protein which is targeted to the medial Golgi apparatus and is necessary for posttranslational modification of dystroglycan. Mutations in this gene have been associated with congenital muscular dystrophy, cognitive disability, and cerebellar cysts. Several alternatively spliced transcript variants of this gene have been described, but the full-length nature of some of these variants has not been determined. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:17997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17997) · Entrez [79147](https://www.ncbi.nlm.nih.gov/gene/79147) · UniProt [Q9H9S5](https://www.uniprot.org/uniprotkb/Q9H9S5) · Ensembl [ENSG00000181027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181027)

## Data

Gene col 11159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11159); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11159]; `tensor/DDL_lfc|DDL_z.npy` [11159]; `embed/gene_vectors.npy` [11159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11159 or target_col == 11159). Every well: [[FKRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
