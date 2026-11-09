---
symbol: "NXPH1"
type: "gene"
col: 4355
ensembl_id: "ENSG00000122584"
name: "neurexophilin 1"
location: "7p21.3"
module: 19
arm: "+"
pooled_cpm: 2.84
n_lines_expressing: 35
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NXPH1

*neurexophilin 1* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.27× (z +22.6, q 0e+00, up in 12 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.649× (z -3.8, q 0.092, down in 5 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.0513×, NCI-H1573 0.0808×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0534×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.0561×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENPEP]] (+0.71, fdr 1e-05), [[LINC02398]] (+0.69, fdr 1e-05), [[PDE8B]] (+0.69, fdr 7e-06); moves opposite to [[GTF2E2]] (-0.54, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ENPEP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.27×** | +22.6 | 0e+00 | 12/19 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.37×** | +12.3 | 2e-32 | 2/3 (BT-474, NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +11.8 | 1e-29 | 11/22 (SHP-77, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +9.9 | 5e-21 | 2/9 (NCI-H2030, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.23×** | +9.4 | 4e-19 | 3/6 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.83×** | +9.1 | 1e-17 | 15/25 (SK-MEL-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.9 | 3e-10 | 11/30 (SW48, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +6.7 | 1e-09 | 14/29 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +6.3 | 2e-08 | 6/19 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +5.6 | 1e-06 | 9/22 (HCT15, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +4.8 | 7e-05 | 6/20 (SW48, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +4.8 | 9e-05 | 7/18 (NCI-H23, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.002 | 2/15 (SW480, PANC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +3.8 | 0.005 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +3.8 | 0.006 | 3/29 (LS 180, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.78×** | +3.6 | 0.013 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.015 | 6/28 (BT-474, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.024 | 2/18 (PANC-1, COLO 205) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.028 | 1/23 (SW48) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.034 | 3/21 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4355.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.0513×, NCI-H1573 0.0808×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0534×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.0561×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.649×** | -3.8 | 0.092 | 5/15 (NCI-H1792, HCT15, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | 0.680× | -3.4 | 0.18 | 4/29 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.685× | -3.3 | 0.18 | 7/25 (HCT15, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 8.40 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0534× (z -9.2) |
| [[HCT15 (line)]] | alt | 4.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 7.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0808× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -12.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +8.8) | — |
| [[A-172 (line)]] | wt | 0.842 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.625 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.779 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.830 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.720 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.817 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.927 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENPEP]] | +0.71 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[LINC02398]] | +0.69 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[PDE8B]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ANO3]] | +0.68 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[TPRG1]] | +0.68 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[LINC02208]] | +0.67 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[AQP4-AS1]] | +0.66 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[CHODL]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[UNC79]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[IQCM]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[LINC02755]] | +0.64 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[DPH6-DT]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.54 | -0.53 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NXPH1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZSCAN31]] | B | ZSCAN31 activity raises NXPH1's level | lines that do not express ZSCAN31 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without ZSCAN31 | 0.075 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC02306]] | B | LINC02306 activity raises NXPH1's level | lines that do not express LINC02306 (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without LINC02306 | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[BRINP3]] | B | BRINP3 activity raises NXPH1's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without BRINP3 | 0.093 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPEP]] | B | NXPH1 activity strengthens ENPEP's drug response | lines that do not express NXPH1 (7) vs lines expressing it (15) | the lines without NXPH1 respond 1.13× as strongly (z diff +0.17); strongest at Belinostat 5 µM: 0.56x vs 0.18x (z diff +4.4) | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.3, 24.8); signed map (36.6, 11.2). **Vector** length 42.8, 7.60% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +22.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +1.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.9 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.7 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.1 | -0.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.0 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | +0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | neurexophilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:8,433,609-8,752,961 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Neurexophilins |
| Matched by | ensembl_id |

**Function**, from UniProt [P58417](https://www.uniprot.org/uniprotkb/P58417) (Neurexophilin-1):

> May be signaling molecules that resemble neuropeptides and that act by binding to alpha-neurexins and possibly other receptors.

**Summary**, from NCBI Gene [30010](https://www.ncbi.nlm.nih.gov/gene/30010):

> This gene is a member of the neurexophilin family and encodes a secreted protein with a variable N-terminal domain, a highly conserved, N-glycosylated central domain, a short linker region, and a cysteine-rich C-terminal domain. This protein forms a very tight complex with alpha neurexins, a group of proteins that promote adhesion between dendrites and axons. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20693) · Entrez [30010](https://www.ncbi.nlm.nih.gov/gene/30010) · UniProt [P58417](https://www.uniprot.org/uniprotkb/P58417) · Ensembl [ENSG00000122584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122584)

## Data

Gene col 4355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4355); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4355]; `tensor/DDL_lfc|DDL_z.npy` [4355]; `embed/gene_vectors.npy` [4355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4355 or target_col == 4355). Every well: [[NXPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NXPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
