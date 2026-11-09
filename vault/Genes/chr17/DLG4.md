---
symbol: "DLG4"
type: "gene"
col: 5335
ensembl_id: "ENSG00000132535"
name: "discs large MAGUK scaffold protein 4"
location: "17p13.1"
module: 53
arm: "+"
pooled_cpm: 15.25
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# DLG4

*discs large MAGUK scaffold protein 4* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.20× (z +7.9, q 1e-12, up in 14 of 44 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +5.6, q 3e-06, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.535× (z -7.8, q 4e-12, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASGR1]] (+0.76, fdr 7e-06, ⚠ same locus), [[MIR9-1HG]] (+0.65, fdr 7e-06), [[SLC9A5]] (+0.65, fdr 7e-06), [[LAG3]] (+0.64, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); 3 go from it, the strongest it → [[MIR9-1HG]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.20×** | +7.9 | 1e-12 | 14/44 (A498, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.1 | 2e-07 | 10/22 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.0 | 4e-07 | 19/37 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +5.6 | 3e-06 | 23/43 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.9 | 9e-05 | 20/43 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.7 | 3e-04 | 18/43 (A-172, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.21 | 10/44 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.535×** | -7.8 | 4e-12 | 29/43 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -6.7 | 8e-09 | 27/43 (MIA PaCa-2, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -6.1 | 2e-07 | 25/43 (H4, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -6.1 | 2e-07 | 25/43 (SW 900, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.622×** | -5.9 | 3e-07 | 25/44 (SNU-1, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -5.9 | 3e-07 | 25/44 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -5.8 | 6e-07 | 24/41 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.699×** | -4.5 | 6e-04 | 19/44 (MIA PaCa-2, SW 900, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.706×** | -4.3 | 9e-04 | 20/44 (SW 900, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.708×** | -4.3 | 9e-04 | 18/44 (A-172, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.728×** | -4.0 | 0.004 | 18/44 (NCI-H2030, NCI-H1573, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.772×** | -3.2 | 0.058 | 18/44 (hTERT-HPNE, SW 900, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.775×** | -3.2 | 0.062 | 13/43 (H4, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -3.1 | 0.067 | 16/44 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 40.0 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -10.6) |
| [[H4 (line)]] | wt | 16.1 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.101× (z -9.6) |
| [[LoVo (line)]] | wt | 8.26 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 30.5× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 7.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +18.0) | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.115× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.171× (z -9.0) |
| [[SW 900 (line)]] | alt | 44.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -13.1) |
| [[Hs 766T (line)]] | wt | 9.01 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0841× (z -10.1) |
| [[J82 (line)]] | alt | 7.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 40.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.5) |
| [[SW480 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0719× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASGR1]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | ⚠ same locus (7.6 kb, same strand: neighbours can correlate without regulation) |
| [[MIR9-1HG]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SLC9A5]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[LAG3]] | +0.64 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[CPT1C]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[HCN2]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 | pathway: Neuronal System |
| [[AZU1]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SAMD14]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[MRC2]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SSC5D]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[NCKAP5L]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SPRED3]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 | pathway: MAPK family signaling cascades |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises DLG4's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 3.23× lower at baseline in the lines without ASGR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[TMEM145]] | B | TMEM145 activity raises DLG4's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without TMEM145 | 0.024 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[FKBP10]] | B | FKBP10 activity raises DLG4's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without FKBP10 | 0.031 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[SSC5D]] | B | SSC5D activity raises DLG4's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.85× lower at baseline in the lines without SSC5D | 0.067 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR9-1HG]] | C | DLG4's natural level weakens MIR9-1HG's drug response | DLG4's natural level across 41 lines (lineage-adjusted; a glimpse) | r -0.74, reverse +0.10; direction not clear | 0.021 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SLC9A5]] | C | DLG4 activity raises SLC9A5's level | lines that do not express DLG4 (3) vs lines expressing it (46) | 1.71× lower at baseline in the lines without DLG4 | 0.072 | ⚠ few lines (3 vs 46); within organs, on part of the lines; also absent: CHST14, NECAB2, DMXL2; maybe low, not absent |
| [[EML3]] | C | DLG4 activity raises EML3's level | lines that do not express DLG4 (3) vs lines expressing it (46) | 1.37× lower at baseline in the lines without DLG4 | 0.091 | ⚠ few lines (3 vs 46); within organs, on part of the lines; also absent: CHST14, NECAB2, DMXL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.0, -17.0); signed map (17.6, 17.3). **Vector** length 89.3, 18.6% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +0.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | discs large MAGUK scaffold protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,187,187-7,219,836 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSD-95, PSD95, SAP90, SAP-90 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Hallmark sets | PEROXISOME, UV_RESPONSE_UP |
| Reactome | 33 pathways, smallest: NrCAM interactions; LGI-ADAM interactions; Activation of Ca-permeable Kainate Receptor |
| Matched by | ensembl_id |

**Function**, from UniProt [P78352](https://www.uniprot.org/uniprotkb/P78352) (MAGUK scaffold protein DLG4):

> Postsynaptic scaffolding protein that plays a critical role in synaptogenesis and synaptic plasticity by providing a platform for the postsynaptic clustering of crucial synaptic proteins (By similarity). Promotes two aspects of synapse maturation: the shift from GluN2B- to GluN2A subunit-containing NMDARs (N-methyl-D-aspartate receptors), and the developmental increase in AMPAR (alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid receptor) transmission (By similarity). Interacts with the …

**Summary**, from NCBI Gene [1742](https://www.ncbi.nlm.nih.gov/gene/1742):

> This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family. It heteromultimerizes with another MAGUK protein, DLG2, and is recruited into NMDA receptor and potassium channel clusters. These two MAGUK proteins may interact at postsynaptic sites to form a multimeric scaffold for the clustering of receptors, ion channels, and associated signaling proteins. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul …

**Accessions** — [HGNC:2903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2903) · Entrez [1742](https://www.ncbi.nlm.nih.gov/gene/1742) · UniProt [P78352](https://www.uniprot.org/uniprotkb/P78352) · Ensembl [ENSG00000132535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132535)

## Data

Gene col 5335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5335); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5335]; `tensor/DDL_lfc|DDL_z.npy` [5335]; `embed/gene_vectors.npy` [5335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5335 or target_col == 5335). Every well: [[DLG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
