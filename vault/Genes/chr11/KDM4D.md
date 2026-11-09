---
symbol: "KDM4D"
type: "gene"
col: 11799
ensembl_id: "ENSG00000186280"
name: "lysine demethylase 4D"
location: "11q21"
module: 10
arm: "+"
pooled_cpm: 3.27
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KDM4D

*lysine demethylase 4D* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +13.5, q 1e-38, up in 30 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.600× (z -5.2, q 9e-05, down in 14 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF407-AS1]] (+0.69, fdr 7e-06), [[ACTG1P17]] (+0.69, fdr 7e-06), [[TMEM186]] (+0.65, fdr 1e-05); moves opposite to [[TRAF7]] (-0.57, fdr 6e-05), [[PLXND1]] (-0.55, fdr 2e-04), [[NDRG3]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF573]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +13.5 | 1e-38 | 30/35 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.89×** | +9.6 | 1e-19 | 19/44 (A-427, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +7.3 | 4e-11 | 22/41 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +6.5 | 1e-08 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.60×** | +5.0 | 5e-05 | 10/44 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 9e-05 | 12/34 (C32, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.010 | 8/45 (HS-578T, HOP62, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.018 | 5/44 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.027 | 12/37 (HS-578T, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.040 | 9/30 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.057 | 7/33 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.057 | 1/29 (SW 1271) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.057 | 7/41 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.059 | 2/17 (SK-MEL-2, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.068 | 3/44 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.080 | 0/44 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.600×** | -5.2 | 9e-05 | 14/42 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -5.1 | 9e-05 | 17/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.592×** | -5.0 | 1e-04 | 13/41 (RPMI-7951, MIA PaCa-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -4.9 | 1e-04 | 11/27 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.662×** | -4.4 | 0.001 | 9/46 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -3.8 | 0.013 | 12/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -3.6 | 0.024 | 11/23 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.715×** | -3.6 | 0.024 | 15/44 (PANC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.719×** | -3.5 | 0.026 | 6/45 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.691×** | -3.5 | 0.026 | 8/40 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |
| [[Sinomenine (drug)]] 0.5 µM |  | **0.724×** | -3.5 | 0.029 | 4/44 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.055 | 7/45 (HOP62, SW48, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -3.2 | 0.057 | 14/42 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.092 | 7/45 (COLO 205, AsPC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.20 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -11.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.229× (z -8.6) |
| [[HOP62 (line)]] | alt | 3.24 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0919× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.39 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0770× (z -8.6) |
| [[SW480 (line)]] | alt | 3.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0561× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407-AS1]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[ACTG1P17]] | +0.69 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[TMEM186]] | +0.65 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[THBS4]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[C10orf88]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SCGB2B2]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZNF302]] | +0.61 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[ZNF665]] | +0.61 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CKMT2-AS1]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[EMSY-DT]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DNAAF10]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CENPL]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF7]] | -0.57 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[PLXND1]] | -0.55 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[NDRG3]] | -0.54 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[NOMO1]] | -0.54 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[SH3GLB2]] | -0.51 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[COL18A1]] | -0.51 | -0.63 / -0.29 | both halves | 2e-04 |  |
| [[TBCD]] | -0.50 | -0.50 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF573]] | C | ZNF573 activity raises KDM4D's level | lines that do not express ZNF573 (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without ZNF573 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with FBXW7; also absent: ZNF540, ZNF675, ZNF571 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.0, 21.9); signed map (26.9, -13.7). **Vector** length 46.4, 5.59% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +13.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.1 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.7 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 4D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,973,709-94,999,519 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10251; previously JMJD2D |
| Gene groups (HGNC) | Lysine demethylase 4 family |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6B0I6](https://www.uniprot.org/uniprotkb/Q6B0I6) (Lysine-specific demethylase 4D):

> Histone demethylase that specifically demethylates 'Lys-9' of histone H3, thereby playing a central role in histone code. Does not demethylate histone H3 'Lys-4', H3 'Lys-27', H3 'Lys-36' nor H4 'Lys-20'. Demethylates both di- and trimethylated H3 'Lys-9' residue, while it has no activity on monomethylated residues. Demethylation of Lys residue generates formaldehyde and succinate.

**Summary**, from NCBI Gene [55693](https://www.ncbi.nlm.nih.gov/gene/55693):

> Enables histone H3K9me2/H3K9me3 demethylase activity. Involved in inflammatory response. Acts upstream of or within several processes, including cellular response to ionizing radiation; double-strand break repair via homologous recombination; and positive regulation of double-strand break repair via nonhomologous end joining. Located in site of double-strand break. Biomarker of nephroblastoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25498) · Entrez [55693](https://www.ncbi.nlm.nih.gov/gene/55693) · UniProt [Q6B0I6](https://www.uniprot.org/uniprotkb/Q6B0I6) · Ensembl [ENSG00000186280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186280)

## Data

Gene col 11799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11799); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11799]; `tensor/DDL_lfc|DDL_z.npy` [11799]; `embed/gene_vectors.npy` [11799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11799 or target_col == 11799). Every well: [[KDM4D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM4D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
