---
symbol: "ZKSCAN4"
type: "gene"
col: 11930
ensembl_id: "ENSG00000187626"
name: "zinc finger with KRAB and SCAN domains 4"
location: "6p22.1"
module: 89
arm: "+"
pooled_cpm: 2.96
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# ZKSCAN4

*zinc finger with KRAB and SCAN domains 4* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 6.84× (z +20.9, q 0e+00, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.489× (z -7.8, q 4e-12, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB4]] (+0.68, fdr 7e-06), [[ZNF2]] (+0.66, fdr 1e-05), [[ZBTB6]] (+0.66, fdr 1e-05); moves opposite to [[RELL1]] (-0.56, fdr 3e-05), [[ODF2]] (-0.53, fdr 1e-05), [[LMBR1]] (-0.51, fdr 3e-04).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZNF429]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **6.84×** | +20.9 | 0e+00 | 38/43 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +8.4 | 2e-14 | 12/45 (SW480, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +7.7 | 2e-12 | 17/33 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +6.0 | 3e-07 | 17/37 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +5.8 | 7e-07 | 13/37 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.5 | 5e-06 | 7/18 (LS 180, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +5.0 | 4e-05 | 13/46 (J82, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.37×** | +4.9 | 7e-05 | 8/34 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.8 | 1e-04 | 7/45 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.5 | 3e-04 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +4.3 | 8e-04 | 6/40 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +4.3 | 1e-03 | 6/46 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.001 | 4/29 (HCT15, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.002 | 7/45 (A-427, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.003 | 5/42 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.003 | 9/44 (HEC-1-A, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.004 | 7/45 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -7.8 | 4e-12 | 23/44 (PANC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.509×** | -7.3 | 6e-11 | 21/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -6.2 | 1e-07 | 11/30 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.580×** | -5.7 | 2e-06 | 12/22 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.722×** | -3.5 | 0.044 | 12/45 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.800×** | -3.4 | 0.056 | 7/45 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.743× | -3.1 | 0.15 | 7/42 (C-33 A, Panc 03.27, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.750× | -3.0 | 0.17 | 0/44 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 2.40 | 1 | 2 | [[Auranofin (drug)]] 5 µM 11.9× (z +8.6) | [[Dihydroartemisinin (drug)]] 0.05 µM 0.0717× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 2.89 | 1 | 2 | [[Auranofin (drug)]] 5 µM 8.47× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -9.5) |
| [[PANC-1 (line)]] | alt | 3.00 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0426× (z -14.9) |
| [[C32 (line)]] | wt | 2.70 | 1 | 1 | [[Auranofin (drug)]] 5 µM 35.0× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0351× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 2.48 | 1 | 1 | [[Auranofin (drug)]] 5 µM 14.0× (z +9.2) | [[Ivermectin (drug)]] 0.5 µM 0.0904× (z -8.5) |
| [[SW480 (line)]] | alt | 3.58 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.98× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.0628× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 4.68 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.6× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 2.11 | 1 | 0 | [[Auranofin (drug)]] 5 µM 25.6× (z +9.1) | — |
| [[LoVo (line)]] | wt | 1.37 | 1 | 0 | [[Auranofin (drug)]] 5 µM 22.9× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 3.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0503× (z -10.3) ⚠ cell-cycle shift, explains ~2% of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.42 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.2× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 1 | 0 | [[Auranofin (drug)]] 5 µM 70.2× (z +11.9) | — |
| [[A-172 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB4]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZNF2]] | +0.66 | +0.74 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZBTB6]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 | same gene group |
| [[ALKBH3]] | +0.66 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[RBAK]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 | same gene group |
| [[SLC4A1AP]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[HIKESHI]] | +0.64 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[ZNF383]] | +0.63 | +0.69 / +0.54 | both halves | 1e-05 | same gene group |
| [[PEX12]] | +0.63 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ZNF691]] | +0.62 | +0.68 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZSCAN20]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 | same gene group; STRING 819 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL1]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ODF2]] | -0.53 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[LMBR1]] | -0.51 | -0.64 / -0.29 | both halves | 3e-04 |  |
| [[GRK6]] | -0.51 | -0.61 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF429]] | B | ZNF429 activity raises ZKSCAN4's level | lines that do not express ZNF429 (11) vs lines expressing it (39) | 1.37× lower at baseline in the lines without ZNF429 | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF724, ENSG00000283201, ZNF254 |
| [[ZNF829]] | B | ZNF829 activity raises ZKSCAN4's level | lines that do not express ZNF829 (20) vs lines expressing it (30) | 1.20× lower at baseline in the lines without ZNF829 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF568, ZNF880, ZNF625 |
| [[ZNF790]] | B | ZNF790 activity raises ZKSCAN4's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without ZNF790 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569 |
| [[ZNF606]] | B | ZNF606 activity raises ZKSCAN4's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without ZNF606 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |
| [[ZNF223]] | B | ZNF223 activity raises ZKSCAN4's level | lines that do not express ZNF223 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without ZNF223 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF284, TGFB1I1, ZNF891 |
| [[ZNF573]] | C | ZNF573 activity raises ZKSCAN4's level | lines that do not express ZNF573 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without ZNF573 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with FBXW7; also absent: ZNF540, ZNF675, ZNF571; its own permutation p |
| [[ZNF419]] | C | ZNF419 activity raises ZKSCAN4's level | lines that do not express ZNF419 (4) vs lines expressing it (46) | 1.47× lower at baseline in the lines without ZNF419 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: UBA6-DT, ENSG00000251379, ZNF264 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.7, 7.3); signed map (-5.8, -19.1). **Vector** length 57.9, 7.81% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +20.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.7 | -3.1 |
|  | [[Pimozide (drug)]] 5 µM |  | -0.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger with KRAB and SCAN domains 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,241,697-28,252,269 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p373c6.1, P1P373C6, FLJ32136, ZSCAN36; previously ZNF307, ZNF427 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969J2](https://www.uniprot.org/uniprotkb/Q969J2) (Zinc finger protein with KRAB and SCAN domains 4):

> May be involved in the transcriptional activation of MDM2 and EP300 genes.

**Summary**, from NCBI Gene [387032](https://www.ncbi.nlm.nih.gov/gene/387032):

> Enables identical protein binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13854) · Entrez [387032](https://www.ncbi.nlm.nih.gov/gene/387032) · UniProt [Q969J2](https://www.uniprot.org/uniprotkb/Q969J2) · Ensembl [ENSG00000187626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187626)

## Data

Gene col 11930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11930); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11930]; `tensor/DDL_lfc|DDL_z.npy` [11930]; `embed/gene_vectors.npy` [11930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11930 or target_col == 11930). Every well: [[ZKSCAN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZKSCAN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
