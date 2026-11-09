---
symbol: "NFS1"
type: "gene"
col: 14385
ensembl_id: "ENSG00000244005"
name: "NFS1 cysteine desulfurase"
location: "20q11.22"
module: 12
arm: "+"
pooled_cpm: 20.05
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NFS1

*NFS1 cysteine desulfurase* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.57× (z +8.4, q 2e-14, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.699× (z -6.6, q 2e-08, down in 25 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.701× (z -6.6, q 2e-08, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARS2]] (+0.58, fdr 1e-05), [[CCDC51]] (+0.56, fdr 1e-05), [[TEX264]] (+0.55, fdr 1e-05); moves opposite to [[ERO1B]] (-0.44, fdr 3e-04), [[PDIA3P1]] (-0.40, fdr 3e-04), [[LYST]] (-0.40, fdr 2e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPATC1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +8.4 | 2e-14 | 35/48 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +7.8 | 2e-12 | 32/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.4 | 3e-08 | 24/48 (CFPAC-1, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +6.4 | 3e-08 | 23/43 (NCI-H23, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +5.8 | 8e-07 | 20/47 (HepG2/C3A, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +5.3 | 1e-05 | 22/47 (NCI-H1792, NCI-H460, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.32×** | +5.0 | 4e-05 | 12/32 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +4.5 | 4e-04 | 12/47 (HS-578T, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.26×** | +4.1 | 0.003 | 15/43 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.009 | 11/48 (H4, NCI-H1573, …) | two highest doses |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.015 | 6/46 (HCT15, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.20×** | +3.4 | 0.027 | 16/47 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.036 | 9/45 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +3.3 | 0.036 | 12/47 (KATO III, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | 1.19× | +3.3 | 0.038 | 12/41 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.045 | 7/47 (NCI-H1573, C-33 A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.045 | 3/47 (PANC-1, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.053 | 5/48 (SNU-423, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.072 | 7/44 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.098 | 6/43 (LS 180, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.699×** | -6.6 | 2e-08 | 25/47 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -6.6 | 2e-08 | 26/47 (SHP-77, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -6.4 | 2e-08 | 25/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -6.3 | 4e-08 | 24/47 (SW1417, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -4.9 | 1e-04 | 23/43 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.778×** | -4.6 | 4e-04 | 18/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.817×** | -3.7 | 0.016 | 15/47 (NCI-H23, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.824×** | -3.6 | 0.026 | 18/47 (HepG2/C3A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.833× | -3.2 | 0.079 | 18/47 (AsPC-1, J82, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.9) ⚠ cell-cycle shift, explains ~10% of this change | [[Digitoxin (drug)]] 5 µM 0.421× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.441× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 17.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.1) ⚠ cell-cycle shift, explains ~10% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -9.5) |
| [[A-172 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[A498 (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.5) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0521× (z -14.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +9.5) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[HS-578T (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.0) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[LoVo (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.9) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.1) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[LS 180 (line)]] | wt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.30× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +19.9) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.0) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARS2]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CCDC51]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TEX264]] | +0.55 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[COASY]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 | pathway: Metabolism of vitamins and cofactors |
| [[MEN1]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[WDR24]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CHERP]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[AAR2]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[NDUFA8]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[MCAT]] | +0.51 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[UPF1]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[BCS1L]] | +0.50 | +0.36 / +0.59 | both halves | 1e-04 | pathway: Aerobic respiration and respiratory electron transport |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERO1B]] | -0.44 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[PDIA3P1]] | -0.40 | -0.27 / -0.31 | both halves | 3e-04 |  |
| [[LYST]] | -0.40 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[GPR137C]] | -0.40 | -0.07 / -0.39 | ⚠ not reproduced | 0.004 |  |
| [[TAX1BP1]] | -0.40 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATC1L]] | B | SPATC1L activity raises NFS1's level | lines that do not express SPATC1L (10) vs lines expressing it (40) | 1.22× lower at baseline in the lines without SPATC1L | 0.085 | ⚠ within organs, on part of the lines; also absent: TIAM1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.277). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.0, -4.7); signed map (-12.5, -26.1). **Vector** length 74.3, 13.0% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +3.6 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.4 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | NFS1 cysteine desulfurase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,668,052-35,699,355 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NifS, IscS |
| Gene groups (HGNC) | Mitochondrial iron-sulfur assembly components |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 9 pathways, smallest: Molybdenum cofactor biosynthesis; Mitochondrial iron-sulfur cluster biogenesis; Maturation of TCA enzymes and regulation of TCA cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y697](https://www.uniprot.org/uniprotkb/Q9Y697) (Cysteine desulfurase):

> [Isoform Mitochondrial]: Cysteine desulfurase, of the core iron-sulfur cluster (ISC) assembly complex, that catalyzes the desulfuration of L-cysteine to L-alanine, as component of the cysteine desulfurase complex, leading to the formation of a cysteine persulfide intermediate at the active site cysteine residue and participates in the [2Fe-2S] clusters assembly on the scaffolding protein ISCU. The persulfide is then transferred on the flexible Cys loop from the catalytic site of NFS1 to the …

**Summary**, from NCBI Gene [9054](https://www.ncbi.nlm.nih.gov/gene/9054):

> Iron-sulfur clusters are required for the function of many cellular enzymes. The proteins encoded by this gene supply inorganic sulfur to these clusters by removing the sulfur from cysteine, creating alanine in the process. This gene uses alternate in-frame translation initiation sites to generate mitochondrial forms and cytoplasmic/nuclear forms. Selection of the alternative initiation sites is determined by the cytosolic pH. The encoded proteins belong to the class-V family of pyridoxal …

**Accessions** — [HGNC:15910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15910) · Entrez [9054](https://www.ncbi.nlm.nih.gov/gene/9054) · UniProt [Q9Y697](https://www.uniprot.org/uniprotkb/Q9Y697) · Ensembl [ENSG00000244005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244005)

## Data

Gene col 14385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14385); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14385]; `tensor/DDL_lfc|DDL_z.npy` [14385]; `embed/gene_vectors.npy` [14385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14385 or target_col == 14385). Every well: [[NFS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
