---
symbol: "ZFP2"
type: "gene"
col: 12749
ensembl_id: "ENSG00000198939"
name: "ZFP2 zinc finger protein"
location: "5q35.3"
module: 10
arm: "+"
pooled_cpm: 2.91
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZFP2

*ZFP2 zinc finger protein* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +9.9, q 3e-20, up in 19 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.292× (z -10.9, q 6e-25, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9B1]] (+0.70, fdr 7e-06), [[ABCA17P]] (+0.70, fdr 7e-06), [[TMCC1-DT]] (+0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CHD5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +9.9 | 3e-20 | 19/29 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +8.7 | 7e-16 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +6.2 | 1e-07 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.2 | 1e-07 | 1/10 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.6 | 3e-06 | 5/15 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +4.5 | 6e-04 | 13/45 (LoVo, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.4 | 8e-04 | 8/43 (A498, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.63×** | +4.1 | 0.003 | 7/38 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.36×** | +3.8 | 0.007 | 3/44 (NCI-H2347, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.008 | 6/35 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +3.7 | 0.013 | 2/6 (PANC-1, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.013 | 7/20 (BT-474, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.013 | 8/33 (C-33 A, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.015 | 8/42 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.017 | 3/21 (LoVo, NCI-H460, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.020 | 5/45 (C32, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.020 | 8/44 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.076 | 4/29 (SK-MEL-2, C-33 A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.079 | 5/41 (HOP62, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.292×** | -10.9 | 6e-25 | 27/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.466×** | -6.8 | 4e-09 | 18/41 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.592×** | -4.6 | 6e-04 | 18/36 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.585×** | -4.6 | 7e-04 | 13/44 (NCI-H23, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.623×** | -4.0 | 0.006 | 10/38 (PANC-1, SW48, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.658×** | -3.7 | 0.020 | 11/43 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.668×** | -3.6 | 0.029 | 13/45 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.668×** | -3.4 | 0.043 | 8/45 (HepG2/C3A, A549, …) | top dose only | plate-row cell shift |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.696×** | -3.2 | 0.085 | 9/44 (NCI-H2030, BT-474, …) | inconsistent across doses |  |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.711× | -3.0 | 0.15 | 9/39 (HCT15, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.76 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0444× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.17 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0682× (z -11.4) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -8.7) |
| [[A-172 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.865 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.886 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.980 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9B1]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ABCA17P]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[TMCC1-DT]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[DDX59-AS1]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LMO7-AS1]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD20A21P]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ADAP2]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PSMG3-AS1]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[C19orf18]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[NSMCE1-DT]] | +0.62 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[LINC02951]] | +0.61 | +0.65 / +0.40 | both halves | 4e-05 |  |
| [[LINC02609]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD5]] | B | CHD5 activity raises ZFP2's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without CHD5 | 0.043 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[ABCA17P]] | B | ABCA17P activity raises ZFP2's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without ABCA17P | 0.051 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[FAM66C]] | B | FAM66C activity raises ZFP2's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without FAM66C | 0.073 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.4, 30.9); signed map (35.8, -8.8). **Vector** length 46.0, 5.16% of its response variance represented; |z| ≥ 3 in 1,189 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.1 | +0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.1 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +4.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -10.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -1.4 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Allopurinol (drug)]] 0.05 µM |  | -0.9 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.5 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -0.8 | -0.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -0.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ZFP2 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,895,898-178,933,212 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21628, ZNF751 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN57](https://www.uniprot.org/uniprotkb/Q6ZN57) (Zinc finger protein ZFP2):

> Probable transcription factor involved in neuronal differentiation and/or phenotypic maintenance.

**Summary**, from NCBI Gene [80108](https://www.ncbi.nlm.nih.gov/gene/80108):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26138) · Entrez [80108](https://www.ncbi.nlm.nih.gov/gene/80108) · UniProt [Q6ZN57](https://www.uniprot.org/uniprotkb/Q6ZN57) · Ensembl [ENSG00000198939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198939)

## Data

Gene col 12749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12749); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12749]; `tensor/DDL_lfc|DDL_z.npy` [12749]; `embed/gene_vectors.npy` [12749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12749 or target_col == 12749). Every well: [[ZFP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
