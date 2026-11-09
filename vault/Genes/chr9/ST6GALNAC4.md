---
symbol: "ST6GALNAC4"
type: "gene"
col: 5915
ensembl_id: "ENSG00000136840"
name: "ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 4"
location: "9q34.11"
module: 68
arm: "-"
pooled_cpm: 4.51
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# ST6GALNAC4

*ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 4* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.39× (z +10.6, q 2e-23, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.377× (z -16.7, q 0e+00, down in 33 of 36 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC6]] (+0.76, fdr 7e-06, ⚠ same locus), [[TRABD]] (+0.75, fdr 1e-05), [[PACC1]] (+0.72, fdr 1e-05), [[ANKRD27]] (+0.70, fdr 4e-05); moves opposite to [[UNK]] (-0.72, fdr 2e-05), [[RC3H2]] (-0.72, fdr 3e-05), [[PBLD]] (-0.70, fdr 4e-04).
> It sits in the **-** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARHGAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.39×** | +10.6 | 2e-23 | 33/45 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +9.5 | 5e-19 | 33/45 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +9.3 | 2e-18 | 28/44 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +8.7 | 7e-16 | 2/5 (SNU-423, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +7.4 | 2e-11 | 20/34 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +7.3 | 2e-11 | 21/41 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.1 | 9e-08 | 7/21 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +5.7 | 1e-06 | 17/45 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +5.6 | 1e-06 | 16/45 (SW480, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.9 | 0.006 | 7/22 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +3.6 | 0.017 | 1/11 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.063 | 5/46 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.2 | 0.063 | 7/29 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.0 | 0.092 | 9/44 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.61×** | +3.0 | 0.092 | 6/32 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.092 | 3/34 (NCI-H2347, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5915.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.377×** | -16.7 | 0e+00 | 33/36 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.367×** | -11.7 | 3e-29 | 32/40 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.460×** | -9.4 | 9e-19 | 19/34 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -8.5 | 2e-15 | 28/38 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.580×** | -6.6 | 4e-09 | 18/42 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -6.5 | 8e-09 | 16/44 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.670×** | -4.9 | 9e-05 | 11/40 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.550×** | -3.8 | 0.010 | 11/37 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.737×** | -3.6 | 0.023 | 9/22 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -3.5 | 0.030 | 6/31 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.039 | 10/46 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -3.2 | 0.068 | 9/35 (SW1417, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.63 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.1) |
| [[A-172 (line)]] | wt | 4.09 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -11.3) |
| [[HOP62 (line)]] | alt | 2.26 | 0 | 2 | — | [[Sinomenine (drug)]] 0.05 µM 0.0610× (z -8.8) |
| [[RKO (line)]] | wt | 42.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0792× (z -19.9) |
| [[A549 (line)]] | wt | 2.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0637× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0468× (z -10.9) |
| [[Hs 766T (line)]] | wt | 8.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -8.7) |
| [[HT-29 (line)]] | alt | 5.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -12.1) |
| [[J82 (line)]] | alt | 3.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 3.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -12.1) |
| [[SHP-77 (line)]] | alt | 9.74 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0640× (z -11.4) |
| [[SW480 (line)]] | alt | 3.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.0) |
| [[A-427 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | +0.76 | +0.72 / +0.64 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; ⚠ same locus (2.5 kb, same strand: neighbours can correlate without regulation) |
| [[TRABD]] | +0.75 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[PACC1]] | +0.72 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.70 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[C20orf27]] | +0.70 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[IMPDH1]] | +0.70 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NEIL2]] | +0.69 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TMEM241]] | +0.69 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[CSNK2A1]] | +0.67 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SH3PXD2B]] | +0.67 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LPCAT1]] | +0.67 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[METAP1]] | +0.67 | +0.72 / +0.32 | both halves | 2e-04 |  |
| [[LRFN3]] | +0.66 | +0.61 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNK]] | -0.72 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[RC3H2]] | -0.72 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[PBLD]] | -0.70 | -0.64 / -0.25 | both halves | 4e-04 |  |
| [[ZNF764]] | -0.69 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.69 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[WAC-AS1]] | -0.69 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[ZBED5]] | -0.68 | -0.61 / -0.29 | both halves | 3e-04 |  |
| [[PATL2]] | -0.68 | -0.63 / -0.32 | both halves | 1e-04 |  |
| [[ZNF341-AS1]] | -0.67 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.67 | -0.69 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[TMEM202-AS1]] | -0.67 | -0.66 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[EFCAB5]] | -0.67 | -0.65 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[C11orf58]] | -0.67 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.67 | -0.64 / -0.20 | both halves | 7e-04 |  |
| [[CREBBP]] | -0.66 | -0.46 / -0.47 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP8]] | B | ARHGAP8 activity lowers ST6GALNAC4's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.11× higher at baseline in the lines without ARHGAP8 | 0.007 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[TOP2A]] | B | TOP2A activity raises ST6GALNAC4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **-** arm (projection on the module's main direction -0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (1.3, 10.4); signed map (-42.0, -8.8). **Vector** length 68.7, 11.2% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +9.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,907,886-127,917,041 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST6GALNACIV, SIAT3C; previously SIAT7D |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 17 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; Termination of O-glycan biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4F1](https://www.uniprot.org/uniprotkb/Q9H4F1) (Alpha-N-acetyl-neuraminyl-2,3-beta-galactosyl-1,3-N-acetyl-galactosaminide alpha-2,6-sialyltransferase):

> Transfers the sialyl group (N-acetyl-alpha-neuraminyl or NeuAc) from CMP-NeuAc to the GalNAc residue on the NeuAc-alpha-2,3-Gal-beta-1,3-GalNAc sequence of glycoproteins and glycolipids forming an alpha-2,6-linkage. Produces branched type disialyl structures by transfer of a sialyl group onto a GalNAc residue inside the backbone core chains. Prefers O-glycans to glycoproteins or glycolipids.

**Summary**, from NCBI Gene [27090](https://www.ncbi.nlm.nih.gov/gene/27090):

> The protein encoded by this gene is a type II membrane protein that catalyzes the transfer of sialic acid from CMP-sialic acid to galactose-containing substrates. The encoded protein prefers glycoproteins rather than glycolipids as substrates and shows restricted substrate specificity, utilizing only the trisaccharide sequence Neu5Ac-alpha-2,3-Gal-beta-1,3-GalNAc. In addition, it is involved in the synthesis of ganglioside GD1A from GM1B. The encoded protein is normally found in the Golgi …

**Accessions** — [HGNC:17846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17846) · Entrez [27090](https://www.ncbi.nlm.nih.gov/gene/27090) · UniProt [Q9H4F1](https://www.uniprot.org/uniprotkb/Q9H4F1) · Ensembl [ENSG00000136840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136840)

## Data

Gene col 5915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5915); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5915]; `tensor/DDL_lfc|DDL_z.npy` [5915]; `embed/gene_vectors.npy` [5915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5915 or target_col == 5915). Every well: [[ST6GALNAC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GALNAC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
