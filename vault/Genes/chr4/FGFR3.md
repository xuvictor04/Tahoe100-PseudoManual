---
symbol: "FGFR3"
type: "gene"
col: 879
ensembl_id: "ENSG00000068078"
name: "fibroblast growth factor receptor 3"
location: "4p16.3"
module: 2
arm: "+"
pooled_cpm: 2.21
n_lines_expressing: 43
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FGFR3

*fibroblast growth factor receptor 3* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.76× (z +19.1, q 0e+00, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.668× (z -4.0, q 0.036, down in 12 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.0973×; ⚠ cell-cycle shift, explains ~19% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.128×); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.0952×); [[Flutamide (drug)]] 0.5 µM in 1 line (A-427 0.0752×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA3F]] (+0.64, fdr 5e-05), [[FGFRL1]] (+0.63, fdr 3e-05), [[RBM38]] (+0.60, fdr 1e-05); moves opposite to [[LARS1]] (-0.53, fdr 3e-05), [[MTREX]] (-0.50, fdr 8e-05), [[DPH5]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[JAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.76×** | +19.1 | 0e+00 | 36/38 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.91×** | +15.9 | 0e+00 | 32/36 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +13.4 | 7e-39 | 2/4 (HepG2/C3A, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.37×** | +12.1 | 9e-32 | 27/37 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.49×** | +11.5 | 8e-29 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.04×** | +11.1 | 1e-26 | 8/12 (CFPAC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +10.1 | 7e-22 | 13/24 (AsPC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.60×** | +9.2 | 3e-18 | 6/8 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +7.0 | 2e-10 | 15/39 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +6.7 | 9e-10 | 9/38 (J82, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.92×** | +6.5 | 4e-09 | 7/21 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.46×** | +5.3 | 4e-06 | 8/24 (NCI-H460, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.0 | 3e-05 | 12/38 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.46×** | +4.7 | 1e-04 | 5/17 (HOP62, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.59×** | +4.6 | 1e-04 | 14/39 (NCI-H460, LoVo, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +4.4 | 5e-04 | 7/31 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.3 | 5e-04 | 8/38 (A498, HEC-1-A, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +3.4 | 0.016 | 1/29 (SW480) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.021 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.021 | 2/34 (Hs 766T, KATO III) | rises with dose | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.021 | 1/16 (J82) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 879.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.0973×; ⚠ cell-cycle shift, explains ~19% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.128×); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.0952×); [[Flutamide (drug)]] 0.5 µM in 1 line (A-427 0.0752×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -4.0 | 0.036 | 12/37 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vandetanib (drug)]] 5 µM |  | 0.729× | -3.1 | 0.42 | 8/39 (A498, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.555× | -3.1 | 0.42 | 4/30 (HOP62, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.12 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.128× (z -10.2) |
| [[A-427 (line)]] | wt | 4.21 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0752× (z -8.7) |
| [[HT-29 (line)]] | alt | 8.89 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0973× (z -10.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LoVo (line)]] | wt | 4.20 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0952× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 0.694 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +8.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.757 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.817 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.125 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.671 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.812 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3F]] | +0.64 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[FGFRL1]] | +0.63 | +0.58 / +0.46 | both halves | 3e-05 | same gene group; pathway: Signaling by FGFR |
| [[RBM38]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PGAP6]] | +0.58 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[JAG2]] | +0.56 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[DGAT1]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RTN4R]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[BCORL1]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[APLP1]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[DMBX1]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[PLXNA3]] | +0.54 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[PDZD4]] | +0.54 | +0.25 / +0.69 | both halves | 4e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARS1]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MTREX]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[DPH5]] | -0.49 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[MCTS1]] | -0.46 | -0.26 / -0.44 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | JAG2 activity raises FGFR3's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without JAG2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[MMP15]] | B | MMP15 activity raises FGFR3's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without MMP15 | 0.086 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.1, -4.9); signed map (-13.7, 34.6). **Vector** length 44.9, 5.85% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.1 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +11.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +19.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -1.5 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,793,293-1,808,872 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CEK2, JTK4, CD333; previously ACH |
| Gene groups (HGNC) | CD molecules; I-set domain containing; Fibroblast growth factor receptor family |
| Hallmark sets | KRAS_SIGNALING_DN, ESTROGEN_RESPONSE_LATE |
| Reactome | 33 pathways, smallest: FGFR3b ligand binding and activation; FGFR3 mutant receptor activation; Signaling by activated point mutants of FGFR3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P22607](https://www.uniprot.org/uniprotkb/P22607) (Fibroblast growth factor receptor 3):

> Tyrosine-protein kinase that acts as a cell-surface receptor for fibroblast growth factors and plays an essential role in the regulation of cell proliferation, differentiation and apoptosis. Plays an essential role in the regulation of chondrocyte differentiation, proliferation and apoptosis, and is required for normal skeleton development. Regulates both osteogenesis and postnatal bone mineralization by osteoblasts. Promotes apoptosis in chondrocytes, but can also promote cancer cell …

**Summary**, from NCBI Gene [2261](https://www.ncbi.nlm.nih.gov/gene/2261):

> This gene encodes a member of the fibroblast growth factor receptor (FGFR) family, with its amino acid sequence being highly conserved between members and among divergent species. FGFR family members differ from one another in their ligand affinities and tissue distribution. A full-length representative protein would consist of an extracellular region, composed of three immunoglobulin-like domains, a single hydrophobic membrane-spanning segment and a cytoplasmic tyrosine kinase domain. The …

**Accessions** — [HGNC:3690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3690) · Entrez [2261](https://www.ncbi.nlm.nih.gov/gene/2261) · UniProt [P22607](https://www.uniprot.org/uniprotkb/P22607) · Ensembl [ENSG00000068078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068078)

## Data

Gene col 879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 879); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 879]; `tensor/DDL_lfc|DDL_z.npy` [879]; `embed/gene_vectors.npy` [879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 879 or target_col == 879). Every well: [[FGFR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGFR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
