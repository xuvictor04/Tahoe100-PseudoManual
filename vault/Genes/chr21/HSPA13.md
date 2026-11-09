---
symbol: "HSPA13"
type: "gene"
col: 7884
ensembl_id: "ENSG00000155304"
name: "heat shock protein family A (Hsp70) member 13"
location: "21q11.2"
module: 42
arm: "+"
pooled_cpm: 64.62
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# HSPA13

*heat shock protein family A (Hsp70) member 13* — 21q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.26× (z +7.6, q 2e-11, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.736× (z -5.3, q 8e-05, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARCN1]] (+0.60, fdr 1e-05), [[USO1]] (+0.60, fdr 1e-05), [[ZNF460]] (+0.55, fdr 2e-05); moves opposite to [[DUS1L]] (-0.46, fdr 9e-05), [[TELO2]] (-0.45, fdr 4e-05), [[CDK10]] (-0.43, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AKT1]], [[AKT2]], [[AKT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +7.6 | 2e-11 | 36/47 (NCI-H23, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +7.5 | 2e-11 | 41/46 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.3 | 2e-05 | 29/46 (NCI-H1573, RKO, …) | two highest doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +5.0 | 6e-05 | 26/45 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +5.0 | 8e-05 | 28/46 (SW480, NCI-H2030, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.21×** | +4.5 | 6e-04 | 20/46 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.20×** | +4.5 | 6e-04 | 22/46 (NCI-H1573, NCI-H23, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 7e-04 | 24/46 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +3.9 | 0.005 | 23/46 (HOP62, NCI-H1573, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.008 | 21/46 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.010 | 20/46 (SW480, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.011 | 15/46 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +3.7 | 0.011 | 20/46 (HOP62, SNU-1, …) | rises with dose | composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.011 | 17/46 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.21×** | +3.4 | 0.026 | 20/46 (HOP62, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.736×** | -5.3 | 8e-05 | 29/46 (J82, HOP62, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.716×** | -4.2 | 0.006 | 26/46 (H4, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.848× | -4.0 | 0.010 | 16/46 (A-427, C32, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.731×** | -4.0 | 0.010 | 20/46 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | 0.853× | -3.8 | 0.015 | 16/46 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.807×** | -3.7 | 0.021 | 19/41 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 91.8 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +15.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.18× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 104 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.58× (z +10.4) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.21× (z +9.0) | — |
| [[KATO III (line)]] | alt | 59.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 40.2 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.49× (z +9.5) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[LS 180 (line)]] | wt | 54.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 83.1 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.12× (z +10.5) | — |
| [[SW480 (line)]] | alt | 68.8 | 1 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.70× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 71.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 49.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C-33 A (line)]] | alt | 72.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 189 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0800× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 90.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 57.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 40.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 55.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.34× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 74.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARCN1]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[USO1]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZNF460]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ARF1]] | +0.55 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[HAX1]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LYSMD3]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ZNF805]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[RWDD2A]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SRP72]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[GOLGA5]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[XBP1]] | +0.51 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[YIPF6]] | +0.51 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUS1L]] | -0.46 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[TELO2]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CDK10]] | -0.43 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[LLGL2]] | -0.41 | -0.38 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKT1]], [[AKT2]], [[AKT3]] | B | AKT1, AKT2, AKT3 activity raises HSPA13's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PRNP]] | C | PRNP activity raises HSPA13's level | lines that do not express PRNP (3) vs lines expressing it (47) | 5.69× lower at baseline in the lines without PRNP | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TFAP2A, ADAMTSL5, KDELR3; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.305). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.5, -17.1); signed map (-57.5, 10.3). **Vector** length 127, 37.7% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +7.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.3 | +5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +5.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +7.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.1 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.2 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Ritonavir (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.5 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q11.2 — chr21:14,371,115-14,383,484 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously STCH |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P48723](https://www.uniprot.org/uniprotkb/P48723) (Heat shock 70 kDa protein 13):

> Has peptide-independent ATPase activity.

**Summary**, from NCBI Gene [6782](https://www.ncbi.nlm.nih.gov/gene/6782):

> The protein encoded by this gene is a member of the heat shock protein 70 family and is found associated with microsomes. Members of this protein family play a role in the processing of cytosolic and secretory proteins, as well as in the removal of denatured or incorrectly-folded proteins. The encoded protein contains an ATPase domain and has been shown to associate with a ubiquitin-like protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11375](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11375) · Entrez [6782](https://www.ncbi.nlm.nih.gov/gene/6782) · UniProt [P48723](https://www.uniprot.org/uniprotkb/P48723) · Ensembl [ENSG00000155304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155304)

## Data

Gene col 7884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7884); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7884]; `tensor/DDL_lfc|DDL_z.npy` [7884]; `embed/gene_vectors.npy` [7884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7884 or target_col == 7884). Every well: [[HSPA13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
