---
symbol: "TCIRG1"
type: "gene"
col: 3161
ensembl_id: "ENSG00000110719"
name: "T cell immune regulator 1, ATPase H+ transporting V0 subunit a3"
location: "11q13.2"
module: 2
arm: "+"
pooled_cpm: 12.4
n_lines_expressing: 45
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TCIRG1

*T cell immune regulator 1, ATPase H+ transporting V0 subunit a3* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[LY-2584702 (tosylate salt) (drug)]] 5 µM: 1.81× (z +3.9, q 0.065, up in 8 of 26 measured lines) ⚠ toxic. The strongest without an alert is [[Celecoxib (drug)]] 0.5 µM: 1.49× (z +3.5, q 0.076, up in 5 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.433× (z -14.6, q 1e-45, down in 34 of 39 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHSD1]] (+0.75, fdr 7e-06), [[SLC26A6]] (+0.72, fdr 1e-05), [[PLPPR2]] (+0.71, fdr 1e-05); moves opposite to [[YARS2]] (-0.63, fdr 4e-04), [[WARS2-AS1]] (-0.59, fdr 2e-04), [[DNAJB14]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OSBPL7]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SIPA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.9 | 0.065 | 8/26 (A-172, J82, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.5 | 0.076 | 10/32 (NCI-H1573, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.076 | 5/41 (HCT15, RKO, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Cytarabine (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.076 | 6/41 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.076 | 7/39 (hTERT-HPNE, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.076 | 8/41 (NCI-H1792, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.076 | 5/38 (J82, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.076 | 6/43 (Hs 766T, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.076 | 9/36 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.433×** | -14.6 | 1e-45 | 34/39 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -11.7 | 3e-29 | 34/41 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.404×** | -8.3 | 2e-14 | 34/40 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -7.6 | 5e-12 | 27/42 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -7.1 | 2e-10 | 29/40 (A549, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.336×** | -7.0 | 2e-10 | 28/39 (RKO, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -5.1 | 4e-05 | 24/39 (CFPAC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -5.0 | 4e-05 | 20/41 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -4.9 | 7e-05 | 22/41 (BT-474, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.685×** | -4.7 | 2e-04 | 19/42 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.688×** | -4.6 | 2e-04 | 23/42 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.714×** | -3.9 | 0.004 | 15/42 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -3.7 | 0.008 | 12/41 (BT-474, A498, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.736×** | -3.6 | 0.015 | 15/41 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.743×** | -3.4 | 0.026 | 7/41 (HS-578T, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.9) |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -10.5) |
| [[J82 (line)]] | alt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.2) |
| [[KATO III (line)]] | alt | 15.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -11.5) |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.2) |
| [[RKO (line)]] | wt | 11.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -12.1) |
| [[SNU-423 (line)]] | alt | 8.00 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.0757× (z -11.1) |
| [[SW 900 (line)]] | alt | 30.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.0) |
| [[A498 (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.6) |
| [[A549 (line)]] | wt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.322× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD1]] | +0.75 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[SLC26A6]] | +0.72 | +0.67 / +0.55 | both halves | 1e-05 | same gene group |
| [[PLPPR2]] | +0.71 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.70 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[RHPN1]] | +0.69 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[ARRB2]] | +0.68 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[AHDC1]] | +0.67 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SKIC2]] | +0.67 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PLD2]] | +0.67 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[DOK4]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MAST3]] | +0.66 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[CEP131]] | +0.65 | +0.66 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS2]] | -0.63 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[WARS2-AS1]] | -0.59 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[DNAJB14]] | -0.59 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[CPSF2]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ST7L]] | -0.57 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[ERCC6L2]] | -0.56 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[RPP38]] | -0.56 | -0.63 / -0.25 | both halves | 4e-04 |  |
| [[GALNT7-DT]] | -0.55 | -0.53 / -0.21 | both halves | 6e-04 |  |
| [[FBXL17]] | -0.55 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[ASXL2]] | -0.55 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[GABPB1-AS1]] | -0.55 | -0.57 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZFX]] | -0.55 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[MCTS1]] | -0.55 | -0.58 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL7]] | B | OSBPL7 activity raises TCIRG1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without OSBPL7 | 0.038 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[GNA15]] | B | GNA15 activity raises TCIRG1's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without GNA15 | 0.069 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIPA1]] | B | TCIRG1 activity lowers SIPA1's level | lines that do not express TCIRG1 (5) vs lines expressing it (45) | 1.15× higher at baseline in the lines without TCIRG1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000255031, SUSD1, MGST2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (5.7, -4.8); signed map (-30.8, 0.2). **Vector** length 77.4, 16.7% of its response variance represented; |z| ≥ 3 in 689 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -0.0 |
|  | [[Cytarabine (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +1.8 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | T cell immune regulator 1, ATPase H+ transporting V0 subunit a3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:68,039,025-68,050,895 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIRC7, OC-116, OC116, ATP6N1C, Atp6i, a3, ATP6V0A3 |
| Gene groups (HGNC) | V-type ATPase subunits; MicroRNA protein coding host genes |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 14 pathways, smallest: Insulin receptor recycling; ROS and RNS production in phagocytes; Transferrin endocytosis and recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13488](https://www.uniprot.org/uniprotkb/Q13488) (V-type proton ATPase 116 kDa subunit a 3):

> Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons (By similarity). V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it is responsible for acidifying the extracellular environment (By similarity). Seems to be directly involved in T-cell …

**Summary**, from NCBI Gene [10312](https://www.ncbi.nlm.nih.gov/gene/10312):

> This gene encodes a subunit of a large protein complex known as a vacuolar H+-ATPase (V-ATPase). The protein complex acts as a pump to move protons across the membrane. This movement of protons helps regulate the pH of cells and their surrounding environment. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, and receptor-mediated endocytosis. V-ATPase is comprised of a cytosolic V1 domain and a transmembrane V0 …

**Accessions** — [HGNC:11647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11647) · Entrez [10312](https://www.ncbi.nlm.nih.gov/gene/10312) · UniProt [Q13488](https://www.uniprot.org/uniprotkb/Q13488) · Ensembl [ENSG00000110719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110719)

## Data

Gene col 3161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3161); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3161]; `tensor/DDL_lfc|DDL_z.npy` [3161]; `embed/gene_vectors.npy` [3161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3161 or target_col == 3161). Every well: [[TCIRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCIRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
