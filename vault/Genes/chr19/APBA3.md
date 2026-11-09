---
symbol: "APBA3"
type: "gene"
col: 225
ensembl_id: "ENSG00000011132"
name: "amyloid beta precursor protein binding family A member 3"
location: "19p13.3"
module: 59
arm: "+"
pooled_cpm: 6.23
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# APBA3

*amyloid beta precursor protein binding family A member 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +11.3, q 6e-27, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.709× (z -4.5, q 0.003, down in 14 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.598× (z -3.5, q 0.055, down in 15 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK3]] (+0.66, fdr 7e-06), [[TMEM106A]] (+0.66, fdr 7e-06), [[WASHC1]] (+0.66, fdr 7e-06); moves opposite to [[PRKDC]] (-0.68, fdr 7e-06), [[RAP1GDS1]] (-0.63, fdr 7e-06), [[IPO7]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +11.3 | 6e-27 | 32/42 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +6.5 | 3e-08 | 24/46 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.1 | 6e-05 | 15/38 (CFPAC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +5.1 | 6e-05 | 8/38 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 15/47 (A498, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.5 | 5e-04 | 13/35 (SW1417, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.003 | 8/39 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +4.0 | 0.005 | 11/39 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.9 | 0.005 | 11/40 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.8 | 0.007 | 5/19 (A-172, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.010 | 6/42 (NCI-H2030, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.013 | 12/47 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.025 | 1/46 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.18× | +3.0 | 0.11 | 5/48 (SHP-77, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 225.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.709×** | -4.5 | 0.003 | 14/47 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.722×** | -4.3 | 0.003 | 12/47 (NCI-H1792, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.723×** | -4.3 | 0.003 | 15/46 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.598×** | -3.5 | 0.055 | 15/41 (RPMI-7951, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.762×** | -3.5 | 0.055 | 8/44 (RPMI-7951, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | **0.833×** | -3.4 | 0.055 | 9/47 (HT-29, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.779×** | -3.3 | 0.073 | 9/47 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.769×** | -3.3 | 0.073 | 4/47 (HS-578T, RKO, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.624×** | -3.3 | 0.073 | 11/45 (NCI-H1792, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.852× | -3.0 | 0.14 | 11/43 (NCI-H460, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 6.92 | 0 | 3 | — | [[APTO-253 (drug)]] 0.05 µM 0.0600× (z -11.1) |
| [[C-33 A (line)]] | alt | 7.01 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 0.5 µM 0.0803× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 6.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 1 | — | [[Fingolimod (hydrochloride) (drug)]] 0.5 µM 0.0507× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 7.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[PANC-1 (line)]] | alt | 6.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +13.2) | — |
| [[A-172 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK3]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TMEM106A]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TCEAL3]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SAT2]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[RAB24]] | +0.62 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[STAP2]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TJAP1]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 | STRING 455 |
| [[PRICKLE3]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PI4KB]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[MITD1]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.68 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[RAP1GDS1]] | -0.63 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[IPO7]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[LRRC20]] | -0.59 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[BANF1]] | -0.58 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.57 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[GMPS]] | -0.57 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[LAMB1]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[GSPT1]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[PARP1]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[IPO5]] | -0.55 | -0.47 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises APBA3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-35.5, -30.5); signed map (-11.0, -0.2). **Vector** length 61.7, 9.19% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +11.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.7 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -1.7 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.6 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -3.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein binding family A member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,750,772-3,761,692 (-) |
| Ensembl biotype | protein_coding |
| Also known as | X11L2, mint3 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O96018](https://www.uniprot.org/uniprotkb/O96018) (Amyloid-beta A4 precursor protein-binding family A member 3):

> May modulate processing of the amyloid-beta precursor protein (APP) and hence formation of APP-beta. May enhance the activity of HIF1A in macrophages by inhibiting the activity of HIF1AN.

**Summary**, from NCBI Gene [9546](https://www.ncbi.nlm.nih.gov/gene/9546):

> The protein encoded by this gene is a member of the X11 protein family. It is an adapter protein that interacts with the Alzheimer's disease amyloid precursor protein. This gene product is believed to be involved in signal transduction processes. This gene is a candidate gene for Alzheimer's disease. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:580) · Entrez [9546](https://www.ncbi.nlm.nih.gov/gene/9546) · UniProt [O96018](https://www.uniprot.org/uniprotkb/O96018) · Ensembl [ENSG00000011132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011132)

## Data

Gene col 225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 225); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 225]; `tensor/DDL_lfc|DDL_z.npy` [225]; `embed/gene_vectors.npy` [225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 225 or target_col == 225). Every well: [[APBA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APBA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
