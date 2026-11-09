---
symbol: "ZNF32"
type: "gene"
col: 9847
ensembl_id: "ENSG00000169740"
name: "zinc finger protein 32"
location: "10q11.21"
module: 12
arm: "+"
pooled_cpm: 4.47
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ZNF32

*zinc finger protein 32* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +7.3, q 2e-10, up in 13 of 20 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.399× (z -12.5, q 6e-33, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM17]] (+0.64, fdr 1e-05), [[ZNF391]] (+0.62, fdr 2e-05), [[RDH14]] (+0.61, fdr 1e-05); moves opposite to [[ODF2]] (-0.58, fdr 3e-05), [[QSOX1]] (-0.49, fdr 4e-05), [[PLCB3]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 2 go from it, the strongest it → [[PATZ1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.3 | 2e-10 | 13/20 (Hs 766T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +7.2 | 2e-10 | 6/7 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.1 | 8e-05 | 12/24 (A498, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.5 | 0.068 | 3/24 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +3.4 | 0.082 | 8/41 (SW480, BT-474, …) | top dose only | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.66× | +3.2 | 0.11 | 3/24 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.39× | +3.2 | 0.11 | 9/38 (A-427, NCI-H23, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.40× | +3.1 | 0.16 | 3/10 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.399×** | -12.5 | 6e-33 | 30/36 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.310×** | -11.2 | 7e-27 | 35/43 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -9.8 | 2e-20 | 23/33 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.375×** | -9.4 | 8e-19 | 30/41 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.396×** | -8.9 | 8e-17 | 30/43 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.402×** | -8.7 | 2e-16 | 26/40 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.460×** | -7.4 | 8e-12 | 24/41 (NCI-H460, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.495×** | -6.7 | 1e-09 | 19/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -6.6 | 3e-09 | 22/36 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.507×** | -6.5 | 4e-09 | 23/41 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -5.3 | 6e-06 | 16/40 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.630×** | -4.4 | 5e-04 | 16/39 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.632×** | -4.4 | 5e-04 | 13/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -3.7 | 0.007 | 14/41 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -3.7 | 0.009 | 10/40 (NCI-H460, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.486×** | -3.6 | 0.011 | 11/31 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.697×** | -3.4 | 0.019 | 16/43 (SK-MEL-2, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.700×** | -3.1 | 0.052 | 5/40 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.555×** | -2.9 | 0.095 | 9/29 (RKO, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.10 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0540× (z -24.2) |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 1.57 | 0 | 2 | — | [[Benztropine (mesylate) (drug)]] 0.5 µM 0.0533× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 8.74 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.1) |
| [[A-427 (line)]] | wt | 8.11 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0726× (z -12.4) |
| [[A549 (line)]] | wt | 4.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 2.97 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0676× (z -8.6) |
| [[J82 (line)]] | alt | 4.09 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0373× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 6.72 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0880× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 3.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0453× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 5.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0864× (z -9.1) |
| [[RKO (line)]] | wt | 7.70 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.108× (z -9.0) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 3.55 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0517× (z -9.3) |
| [[SW480 (line)]] | alt | 2.89 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0501× (z -11.9) |
| [[A-172 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM17]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ZNF391]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 | same gene group |
| [[RDH14]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[FANCF]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RBM45]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ZNF691]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 | same gene group |
| [[DOK1]] | +0.58 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[KAT14]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SLC2A11]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[HEIH]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CUEDC2]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[DPH5]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ODF2]] | -0.58 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[QSOX1]] | -0.49 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[PLCB3]] | -0.49 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[PRKACA]] | -0.48 | -0.27 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity raises ZNF32's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without BOLA3-DT | 0.049 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[TMCC1-DT]] | C | TMCC1-DT activity raises ZNF32's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[C10orf95-AS1]] | C | C10orf95-AS1 activity raises ZNF32's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |
| [[ZBED3]] | C | ZBED3 activity raises ZNF32's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without ZBED3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATZ1]] | C | ZNF32 activity raises PATZ1's level | lines that do not express ZNF32 (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without ZNF32 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF221, ZNF540; its own permutation p |
| [[METAP1D]] | C | ZNF32 activity raises METAP1D's level | lines that do not express ZNF32 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without ZNF32 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF221, ZNF540 |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.363). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.4, 17.4); signed map (-3.6, -29.0). **Vector** length 45.2, 5.74% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +2.8 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.3 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.0 | +1.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -11.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -8.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.6 | -12.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -0.7 | -0.6 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -0.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:43,643,860-43,648,881 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX30, ZNF637, Zfp637 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P17041](https://www.uniprot.org/uniprotkb/P17041) (Zinc finger protein 32):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7580](https://www.ncbi.nlm.nih.gov/gene/7580):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13095) · Entrez [7580](https://www.ncbi.nlm.nih.gov/gene/7580) · UniProt [P17041](https://www.uniprot.org/uniprotkb/P17041) · Ensembl [ENSG00000169740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169740)

## Data

Gene col 9847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9847); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9847]; `tensor/DDL_lfc|DDL_z.npy` [9847]; `embed/gene_vectors.npy` [9847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9847 or target_col == 9847). Every well: [[ZNF32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
