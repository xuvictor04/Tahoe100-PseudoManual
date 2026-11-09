---
symbol: "CAPN3"
type: "gene"
col: 1702
ensembl_id: "ENSG00000092529"
name: "calpain 3"
location: "15q15.1"
module: 10
arm: "+"
pooled_cpm: 3.67
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CAPN3

*calpain 3* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.74× (z +10.1, q 4e-21, up in 28 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.371× (z -7.0, q 1e-09, down in 31 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.432× (z -6.0, q 7e-07, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD17B3]] (+0.76, fdr 7e-06), [[TMEM202-AS1]] (+0.74, fdr 1e-05), [[TMEM232]] (+0.73, fdr 7e-06); moves opposite to [[FAM118A]] (-0.65, fdr 1e-05), [[L2HGDH]] (-0.65, fdr 3e-05), [[NR2C1]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DCT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +10.1 | 4e-21 | 28/34 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +9.3 | 3e-18 | 1/5 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +7.2 | 1e-10 | 3/6 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +6.5 | 1e-08 | 20/32 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.1 | 1e-07 | 19/45 (SW1417, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +6.0 | 2e-07 | 8/20 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +5.0 | 6e-05 | 13/34 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +4.6 | 3e-04 | 14/35 (SK-MEL-2, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.66×** | +4.4 | 8e-04 | 11/40 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.89×** | +4.3 | 8e-04 | 17/38 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.003 | 11/43 (hTERT-HPNE, COLO 205, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +4.0 | 0.003 | 14/44 (SK-MEL-2, LoVo, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.78×** | +4.0 | 0.003 | 13/45 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.78×** | +3.9 | 0.004 | 13/39 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.72×** | +3.8 | 0.005 | 14/41 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.054 | 6/44 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.76×** | +3.1 | 0.054 | 6/40 (hTERT-HPNE, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.054 | 10/40 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.371×** | -7.0 | 1e-09 | 31/45 (SW480, SNU-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -6.0 | 7e-07 | 24/41 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -4.7 | 6e-04 | 20/43 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.563×** | -4.1 | 0.006 | 13/30 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -3.9 | 0.009 | 18/40 (PANC-1, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.581×** | -3.9 | 0.011 | 19/38 (COLO 205, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.576×** | -3.7 | 0.017 | 15/37 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.395×** | -3.4 | 0.040 | 11/32 (COLO 205, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.619×** | -3.4 | 0.040 | 11/45 (NCI-H2030, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.560×** | -3.3 | 0.063 | 11/44 (NCI-H1792, A549, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.26 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 14.0× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B3]] | +0.76 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.74 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[TMEM232]] | +0.73 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.72 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | +0.72 | +0.73 / +0.57 | both halves | 9e-06 |  |
| [[CFAP70]] | +0.72 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.71 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | +0.71 | +0.77 / +0.43 | both halves | 4e-05 |  |
| [[ST8SIA5]] | +0.71 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[EFCAB6]] | +0.70 | +0.73 / +0.49 | both halves | 1e-05 | same gene group |
| [[CCDC30]] | +0.70 | +0.76 / +0.41 | both halves | 4e-05 |  |
| [[MAMDC2-AS1]] | +0.70 | +0.68 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.65 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[L2HGDH]] | -0.65 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NR2C1]] | -0.62 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[CKLF]] | -0.62 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[NBPF3]] | -0.61 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCT]] | B | DCT activity raises CAPN3's level | lines that do not express DCT (42) vs lines expressing it (8) | 1.83× lower at baseline in the lines without DCT | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1 |
| [[TOP2A]] | B | TOP2A activity lowers CAPN3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00278]] | B | LINC00278 activity raises CAPN3's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 1.47× lower at baseline in the lines without LINC00278 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1 |
| [[PSMB5]] | B | PSMB5 activity raises CAPN3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers CAPN3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.9, 15.7); signed map (29.0, -11.4). **Vector** length 63.6, 10.2% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +4.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | calpain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:42,359,498-42,412,949 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CANP3, p94, nCL-1; previously LGMD2, LGMD2A |
| Gene groups (HGNC) | EF-hand domain containing; Calpains |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P20807](https://www.uniprot.org/uniprotkb/P20807) (Calpain-3):

> Calcium-regulated non-lysosomal thiol-protease. Proteolytically cleaves CTBP1 at 'His-409'. Mediates, with UTP25, the proteasome-independent degradation of p53/TP53.

**Summary**, from NCBI Gene [825](https://www.ncbi.nlm.nih.gov/gene/825):

> Calpain, a heterodimer consisting of a large and a small subunit, is a major intracellular protease, although its function has not been well established. This gene encodes a muscle-specific member of the calpain large subunit family that specifically binds to titin. Mutations in this gene are associated with limb-girdle muscular dystrophies type 2A. Alternate promoters and alternative splicing result in multiple transcript variants encoding different isoforms and some variants are ubiquitously …

**Accessions** — [HGNC:1480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1480) · Entrez [825](https://www.ncbi.nlm.nih.gov/gene/825) · UniProt [P20807](https://www.uniprot.org/uniprotkb/P20807) · Ensembl [ENSG00000092529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092529)

## Data

Gene col 1702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1702); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1702]; `tensor/DDL_lfc|DDL_z.npy` [1702]; `embed/gene_vectors.npy` [1702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1702 or target_col == 1702). Every well: [[CAPN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
