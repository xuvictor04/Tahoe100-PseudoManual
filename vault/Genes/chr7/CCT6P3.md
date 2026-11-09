---
symbol: "CCT6P3"
type: "gene"
col: 13968
ensembl_id: "ENSG00000234585"
name: "chaperonin containing TCP1 family member 6A3, pseudogene"
location: "7q11.21"
module: 10
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CCT6P3

*chaperonin containing TCP1 family member 6A3, pseudogene* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.86× (z +19.1, q 0e+00, up in 33 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.153×; ⚠ toxic; transcription drop); [[Sulfatinib (drug)]] 5 µM in 1 line (BT-474 0.0505×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (A-172 0.114×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0806×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX1]] (+0.66, fdr 7e-06), [[CIRBP]] (+0.66, fdr 5e-05), [[SBDSP1-1]] (+0.66, fdr 3e-05); moves opposite to [[AP1S1]] (-0.69, fdr 8e-06), [[AP2S1]] (-0.64, fdr 3e-05), [[BRK1]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZXDA]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +19.1 | 0e+00 | 33/39 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.45×** | +15.3 | 0e+00 | 42/43 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +13.9 | 1e-41 | 34/37 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.05×** | +9.2 | 4e-18 | 28/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +5.9 | 4e-07 | 13/43 (HS-578T, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.4 | 6e-06 | 9/32 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.7 | 2e-04 | 13/43 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.99×** | +4.6 | 3e-04 | 10/44 (SK-MEL-2, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.6 | 3e-04 | 1/8 (SNU-423) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +4.4 | 5e-04 | 13/38 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.002 | 11/46 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.018 | 2/35 (HEC-1-A, MIA PaCa-2) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13968.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.153×; ⚠ toxic; transcription drop); [[Sulfatinib (drug)]] 5 µM in 1 line (BT-474 0.0505×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (A-172 0.114×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0806×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.748× | -3.4 | 0.15 | 14/42 (RKO, C-33 A, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.696× | -3.3 | 0.15 | 7/41 (NCI-H23, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.773× | -3.3 | 0.15 | 10/46 (COLO 205, KATO III, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | 0.707× | -3.2 | 0.15 | 5/43 (A549, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -3.2 | 0.15 | 6/47 (Panc 03.27, SHP-77, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.784× | -3.1 | 0.15 | 13/39 (J82, A-427, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.712× | -3.1 | 0.15 | 1/43 (H4) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.772× | -3.1 | 0.15 | 10/36 (AsPC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.53 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +11.6) | — |
| [[A-172 (line)]] | wt | 5.65 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.114× (z -8.9) |
| [[BT-474 (line)]] | alt | 6.33 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0505× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 6.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +9.5) | — |
| [[J82 (line)]] | alt | 3.75 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0728× (z -8.9) ⚠ cell-cycle shift, explains ~15% of this change |
| [[KATO III (line)]] | alt | 6.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 3.16 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0680× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 3.44 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0806× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 3.47 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0629× (z -8.6) |
| [[PANC-1 (line)]] | alt | 6.29 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 7.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +9.4) | — |
| [[A-427 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX1]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CIRBP]] | +0.66 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[SBDSP1-1]] | +0.66 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[ZNF181]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[GABPB2]] | +0.65 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SEPSECS]] | +0.64 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[KRCC1]] | +0.63 | +0.66 / +0.37 | both halves | 8e-05 |  |
| [[CCT6P1]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 | same gene group |
| [[TSR2]] | +0.63 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ZXDA]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[COQ5]] | +0.62 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[SBDSP1]] | +0.61 | +0.71 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S1]] | -0.69 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[AP2S1]] | -0.64 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[BRK1]] | -0.59 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[RIC1]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NUDT1]] | -0.59 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[UBL5]] | -0.58 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[PIGF]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[IGFBP2]] | -0.58 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[LINC03009-1]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NEDD8]] | -0.57 | -0.67 / -0.26 | both halves | 4e-04 |  |
| [[CTXN1]] | -0.56 | -0.51 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZXDA]] | C | ZXDA activity raises CCT6P3's level | lines that do not express ZXDA (4) vs lines expressing it (46) | 1.25× lower at baseline in the lines without ZXDA | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MBOAT2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-27.1, 8.9); signed map (11.0, -21.8). **Vector** length 51.7, 6.10% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +15.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +19.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.9 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +4.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.0 | +1.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | +0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 family member 6A3, pseudogene |
| Locus type | pseudogene |
| Location | 7q11.21 — chr7:65,064,999-65,073,848 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously CCT6P3 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35137) · Entrez [643180](https://www.ncbi.nlm.nih.gov/gene/643180) · Ensembl [ENSG00000234585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234585)

## Data

Gene col 13968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13968); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13968]; `tensor/DDL_lfc|DDL_z.npy` [13968]; `embed/gene_vectors.npy` [13968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13968 or target_col == 13968). Every well: [[CCT6P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT6P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
