---
symbol: "QARS1"
type: "gene"
col: 10204
ensembl_id: "ENSG00000172053"
name: "glutaminyl-tRNA synthetase 1"
location: "3p21.31"
module: 2
arm: "+"
pooled_cpm: 33.94
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# QARS1

*glutaminyl-tRNA synthetase 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +11.6, q 4e-28, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +7.0, q 6e-10, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.749× (z -6.4, q 1e-07, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL10]] (+0.67, fdr 1e-05), [[EIF3L]] (+0.65, fdr 7e-06), [[VPS26B]] (+0.64, fdr 1e-05); moves opposite to [[DDX52]] (-0.55, fdr 3e-05), [[CRCP]] (-0.51, fdr 4e-05), [[RPL7L1]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRTAP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +11.6 | 4e-28 | 42/44 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +10.2 | 7e-22 | 32/38 (SNU-423, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.0 | 6e-10 | 32/48 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +6.7 | 4e-09 | 36/48 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +6.1 | 1e-07 | 34/48 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +5.8 | 7e-07 | 29/41 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.37×** | +4.9 | 9e-05 | 27/46 (KATO III, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.7 | 0.017 | 17/40 (C32, A498, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.030 | 22/48 (NCI-H2347, RKO, …) | top dose only | low cells (technical?); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.25×** | +3.3 | 0.063 | 17/48 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.23×** | +3.2 | 0.074 | 13/48 (LoVo, SW1417, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.074 | 13/47 (HCT15, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.24×** | +3.1 | 0.074 | 14/47 (C-33 A, RKO, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.078 | 12/45 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.749×** | -6.4 | 1e-07 | 27/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.676×** | -6.1 | 3e-07 | 31/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.711×** | -5.3 | 2e-05 | 32/47 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.748×** | -4.5 | 9e-04 | 25/48 (HEC-1-A, J82, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.778×** | -3.9 | 0.010 | 20/48 (J82, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.644×** | -3.4 | 0.057 | 16/48 (SNU-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.790× | -3.1 | 0.15 | 15/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.824× | -3.0 | 0.18 | 9/47 (SNU-423, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.4) |
| [[PANC-1 (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.101× (z -9.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[HS-578T (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 42.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.2) | — |
| [[RKO (line)]] | wt | 39.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0760× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL10]] | +0.67 | +0.71 / +0.53 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives; STRING 670 |
| [[EIF3L]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | STRING 457 |
| [[VPS26B]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CRAT]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[RPL29]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives; STRING 897 |
| [[PHB2]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[EEF1G]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 | same gene group; STRING 747 |
| [[ABCA2]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.60 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[TMEM183A]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PCYOX1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX52]] | -0.55 | -0.47 / -0.46 | both halves | 3e-05 | same gene group |
| [[CRCP]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[RPL7L1]] | -0.51 | -0.45 / -0.42 | both halves | 4e-05 | STRING 585 |
| [[TRIM56]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[OPA3]] | -0.50 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ZNF75A]] | -0.50 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[EIF3J]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ERVK3-1]] | -0.50 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[LLPH]] | -0.49 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[LINC00106]] | -0.49 | -0.44 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRTAP]] | C | CRTAP activity raises QARS1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without CRTAP | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-29.7, -26.8); signed map (-49.8, -12.0). **Vector** length 72.7, 15.3% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | +3.2 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +11.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.5 | -0.2 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | glutaminyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,095,932-49,105,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously QARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I; MicroRNA protein coding host genes |
| Reactome | 8 pathways, smallest: Mitochondrial tRNA aminoacylation; Cytosolic tRNA aminoacylation; tRNA Aminoacylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P47897](https://www.uniprot.org/uniprotkb/P47897) (Glutamine--tRNA ligase):

> Glutamine--tRNA ligase. Plays a critical role in brain development.

**Summary**, from NCBI Gene [5859](https://www.ncbi.nlm.nih.gov/gene/5859):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. In metazoans, 9 aminoacyl-tRNA synthetases specific for glutamine (gln), glutamic acid (glu), and 7 other amino acids are associated within a multienzyme complex. Although present in eukaryotes, glutaminyl-tRNA …

**Accessions** — [HGNC:9751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9751) · Entrez [5859](https://www.ncbi.nlm.nih.gov/gene/5859) · UniProt [P47897](https://www.uniprot.org/uniprotkb/P47897) · Ensembl [ENSG00000172053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172053)

## Data

Gene col 10204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10204); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10204]; `tensor/DDL_lfc|DDL_z.npy` [10204]; `embed/gene_vectors.npy` [10204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10204 or target_col == 10204). Every well: [[QARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
