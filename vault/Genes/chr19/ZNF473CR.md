---
symbol: "ZNF473CR"
type: "gene"
col: 12910
ensembl_id: "ENSG00000204666"
name: "ZNF473 cis regulating lncRNA"
location: "19q13.33"
module: 37
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# ZNF473CR

*ZNF473 cis regulating lncRNA* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 3.05× (z +8.9, q 4e-16, up in 15 of 21 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +7.9, q 4e-13, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Megestrol (drug)]] 0.05 µM: 0.590× (z -4.4, q 0.006, down in 11 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHKG1]] (+0.66, fdr 7e-06), [[ECT2L]] (+0.64, fdr 7e-06), [[CD247]] (+0.64, fdr 1e-05); moves opposite to [[CSTF2T]] (-0.63, fdr 1e-05), [[DCLRE1A]] (-0.59, fdr 1e-05), [[SNX19]] (-0.55, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KAZN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.05×** | +8.9 | 4e-16 | 15/21 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +7.9 | 4e-13 | 14/33 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.61×** | +7.9 | 4e-13 | 25/42 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +7.3 | 3e-11 | 27/43 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +7.0 | 3e-10 | 19/31 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +7.0 | 3e-10 | 12/21 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +6.7 | 2e-09 | 21/45 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +6.7 | 2e-09 | 6/12 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.91×** | +5.4 | 5e-06 | 12/39 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.78×** | +4.8 | 1e-04 | 15/42 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.72×** | +4.5 | 4e-04 | 7/39 (KATO III, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.75×** | +4.5 | 4e-04 | 0/1 | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +4.3 | 8e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.002 | 9/41 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +3.9 | 0.003 | 12/39 (HEC-1-A, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.005 | 9/39 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.008 | 3/42 (NCI-H460, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.009 | 9/42 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.55×** | +3.6 | 0.009 | 6/43 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.77×** | +3.4 | 0.021 | 1/42 (A-427) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.021 | 6/38 (HT-29, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12910.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Megestrol (drug)]] 0.05 µM |  | **0.590×** | -4.4 | 0.006 | 11/42 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.623×** | -4.0 | 0.021 | 10/44 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.646×** | -3.7 | 0.040 | 9/42 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.651×** | -3.6 | 0.040 | 13/41 (hTERT-HPNE, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.642×** | -3.6 | 0.040 | 6/37 (LOX-IMVI, BT-474, …) | top dose only | position effect removed |
| [[Relugolix (drug)]] 0.5 µM |  | **0.666×** | -3.4 | 0.059 | 8/42 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.668×** | -3.4 | 0.059 | 3/41 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.670×** | -3.2 | 0.086 | 6/39 (SW48, SNU-423, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.692× | -3.1 | 0.13 | 11/42 (H4, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKG1]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ECT2L]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CD247]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[SPDYE5]] | +0.63 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CLEC4A]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PPP1R32]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[BNIPL]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[EOGT-DT]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[BIRC6-AS2-1]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RASA4B]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PP2D1]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZBTB47-AS1]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF2T]] | -0.63 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.59 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SNX19]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[FH]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[CEP41]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CENPBD1P]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RTL6]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ZNF252P-1]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[B3GALT9]] | -0.51 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[PIGO]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[PPP2CA]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[ZNF681]] | -0.51 | -0.38 / -0.51 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KAZN]] | B | KAZN activity raises ZNF473CR's level | lines that do not express KAZN (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without KAZN | 0.070 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, -20.6); signed map (8.8, 5.5). **Vector** length 47.5, 6.12% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +3.0 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | -0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Megestrol (drug)]] 0.05 µM |  | -1.6 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -4.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ZNF473 cis regulating lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.33 — chr19:50,050,589-50,066,793 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ26850 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56021) · Entrez [400710](https://www.ncbi.nlm.nih.gov/gene/400710) · Ensembl [ENSG00000204666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204666)

## Data

Gene col 12910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12910); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12910]; `tensor/DDL_lfc|DDL_z.npy` [12910]; `embed/gene_vectors.npy` [12910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12910 or target_col == 12910). Every well: [[ZNF473CR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF473CR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
