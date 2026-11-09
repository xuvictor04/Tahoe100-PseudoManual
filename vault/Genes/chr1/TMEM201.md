---
symbol: "TMEM201"
type: "gene"
col: 12051
ensembl_id: "ENSG00000188807"
name: "transmembrane protein 201"
location: "1p36.22"
module: 33
arm: "+"
pooled_cpm: 4.35
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TMEM201

*transmembrane protein 201* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.80× (z +21.0, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.80× (z +7.8, q 5e-13, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.780× (z -4.7, q 0.001, down in 9 of 45 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Tofacitinib (drug)]] 0.05 µM: 0.737× (z -4.1, q 0.012, down in 8 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCOF1]] (+0.76, fdr 7e-06), [[BOP1]] (+0.73, fdr 7e-06), [[POLR3H]] (+0.72, fdr 7e-06); moves opposite to [[PIGP]] (-0.61, fdr 4e-05), [[AK9]] (-0.61, fdr 2e-04), [[SMIM14]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **4.80×** | +21.0 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.39×** | +16.3 | 0e+00 | 43/45 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.10×** | +15.1 | 0e+00 | 41/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **2.05×** | +9.2 | 4e-18 | 15/22 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +7.8 | 5e-13 | 22/46 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.78×** | +7.7 | 1e-12 | 21/45 (PANC-1, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.46×** | +7.1 | 1e-10 | 16/39 (NCI-H460, A549, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +6.7 | 2e-09 | 17/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +6.6 | 3e-09 | 15/40 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.66×** | +6.5 | 4e-09 | 14/44 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.58×** | +6.1 | 6e-08 | 11/45 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +5.3 | 5e-06 | 6/44 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.49×** | +5.3 | 5e-06 | 6/19 (HS-578T, CFPAC-1, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +4.8 | 5e-05 | 2/45 (PANC-1, CFPAC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +4.7 | 1e-04 | 14/40 (COLO 205, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 6e-04 | 9/44 (SW480, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.2 | 8e-04 | 9/44 (LOX-IMVI, SK-MEL-2, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +4.1 | 0.001 | 6/43 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.002 | 7/43 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.016 | 1/31 (MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.016 | 4/33 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.021 | 5/38 (NCI-H2030, RPMI-7951, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.040 | 2/32 (MIA PaCa-2, HEC-1-A) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.044 | 3/44 (NCI-H460, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.780×** | -4.7 | 0.001 | 9/45 (COLO 205, KATO III, …) | rises with dose | position effect removed |
| [[Tofacitinib (drug)]] 0.05 µM |  | **0.737×** | -4.1 | 0.012 | 8/44 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.790×** | -3.7 | 0.037 | 7/44 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.765×** | -3.4 | 0.078 | 5/44 (SNU-1, A-172, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.078 | 6/45 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.794× | -3.3 | 0.10 | 4/46 (MIA PaCa-2, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 0.5 µM | ⚠ transcription drop; unreliable plate only | 0.796× | -3.1 | 0.15 | 8/43 (AN3 CA, HEC-1-A, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.789× | -3.0 | 0.15 | 5/45 (SW 900, COLO 205, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.20 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.51× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 1.97 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0586× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 2.92 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0497× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 3.89 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM 0.0562× (z -11.0) |
| [[A-172 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCOF1]] | +0.76 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[BOP1]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[POLR3H]] | +0.72 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SLC19A1]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CCDC88C]] | +0.69 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[TELO2]] | +0.69 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[WNK2]] | +0.69 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[POLRMT]] | +0.68 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[URB2]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[RRP7BP]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[GLB1L2]] | +0.67 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[PGAM5]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGP]] | -0.61 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[AK9]] | -0.61 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[SMIM14]] | -0.59 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[CHD2]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises TMEM201's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without TERT | 0.011 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[GNAZ]] | B | GNAZ activity raises TMEM201's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without GNAZ | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[CBX2]] | B | CBX2 activity raises TMEM201's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without CBX2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[BRSK2]] | B | BRSK2 activity raises TMEM201's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without BRSK2 | 0.037 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[GALNT14]] | B | GALNT14 activity lowers TMEM201's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.44× higher at baseline in the lines without GALNT14 | 0.055 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[FUT4]] | B | FUT4 activity lowers TMEM201's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.52× higher at baseline in the lines without FUT4 | 0.067 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.9, -39.2); signed map (-7.3, -55.2). **Vector** length 52.8, 6.75% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +6.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.1 | +21.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.5 | +16.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.4 | +15.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +2.1 | +9.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +6.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +3.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.8 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 201 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:9,588,911-9,614,877 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP13-15M17.2, NET5, Ima1, SAMP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SNT2](https://www.uniprot.org/uniprotkb/Q5SNT2) (Transmembrane protein 201):

> Critical regulator of angiogenesis and endothelial cell (EC) migration. Promotes the migration of endothelial cells, which is essential for angiogenesis. Interacts with the linker of nucleoskeleton and cytoskeleton (LINC) complex, which plays a vital role in connecting the cell's cytoskeleton to the nuclear envelope. This interaction is essential for maintaining cellular structure and facilitating the movement of endothelial cells, which is critical for proper vascular development. Involved in …

**Summary**, from NCBI Gene [199953](https://www.ncbi.nlm.nih.gov/gene/199953):

> Predicted to enable actin filament binding activity and lamin binding activity. Involved in several processes, including centrosome localization; positive regulation of endothelial cell migration; and protein localization to nuclear envelope. Located in cortical endoplasmic reticulum; nucleus; and spindle pole centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33719) · Entrez [199953](https://www.ncbi.nlm.nih.gov/gene/199953) · UniProt [Q5SNT2](https://www.uniprot.org/uniprotkb/Q5SNT2) · Ensembl [ENSG00000188807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188807)

## Data

Gene col 12051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12051); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12051]; `tensor/DDL_lfc|DDL_z.npy` [12051]; `embed/gene_vectors.npy` [12051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12051 or target_col == 12051). Every well: [[TMEM201 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM201.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
