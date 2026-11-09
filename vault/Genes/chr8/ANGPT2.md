---
symbol: "ANGPT2"
type: "gene"
col: 1679
ensembl_id: "ENSG00000091879"
name: "angiopoietin 2"
location: "8p23.1"
module: 80
arm: "+"
pooled_cpm: 3.4
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# ANGPT2

*angiopoietin 2* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.29× (z +27.9, q 0e+00, up in 34 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.826× (z -6.1, q 8e-07, down in 24 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.533× (z -5.9, q 1e-06, down in 14 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02307]] (+0.86, fdr 7e-06), [[NEB]] (+0.79, fdr 1e-05), [[GUCY2C-AS1]] (+0.75, fdr 3e-05); moves opposite to [[TBC1D24]] (-0.71, fdr 3e-05), [[SLC9A6]] (-0.68, fdr 4e-05), [[WASF3]] (-0.68, fdr 4e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RAB34]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.29×** | +27.9 | 0e+00 | 34/35 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.47×** | +17.4 | 0e+00 | 34/35 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.30×** | +12.6 | 5e-34 | 5/5 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +11.1 | 3e-26 | 0/1 | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +10.9 | 1e-25 | 25/36 (HS-578T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +10.9 | 1e-25 | 10/18 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.35×** | +10.9 | 1e-25 | 27/39 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.61×** | +8.9 | 3e-17 | 26/42 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.7 | 9e-07 | 8/23 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +5.4 | 3e-06 | 16/42 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.2 | 8e-06 | 13/29 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.9 | 4e-05 | 13/46 (A-172, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 5e-04 | 14/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.4 | 5e-04 | 7/32 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +4.3 | 5e-04 | 13/39 (NCI-H460, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +4.3 | 5e-04 | 15/46 (SW480, BT-474, …) | two highest doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 8e-04 | 18/42 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.057 | 8/30 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Trifluridine (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.088 | 3/44 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.088 | 5/44 (C-33 A, SK-MEL-2, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.826×** | -6.1 | 8e-07 | 24/47 (AsPC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.533×** | -5.9 | 1e-06 | 14/44 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.597×** | -4.8 | 3e-04 | 16/44 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -3.5 | 0.076 | 15/45 (SW480, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.688× | -3.2 | 0.14 | 7/44 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.76 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +15.7) | — |
| [[SW480 (line)]] | alt | 16.0 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.0969× (z -10.0) |
| [[LoVo (line)]] | wt | 2.55 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 84.6× (z +19.9) | — |
| [[NCI-H1573 (line)]] | alt | 2.17 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 56.0× (z +17.1) | — |
| [[NCI-H2030 (line)]] | alt | 2.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 59.8× (z +15.0) | — |
| [[SW48 (line)]] | wt | 3.77 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 318× (z +16.9) | — |
| [[A-172 (line)]] | wt | 4.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +13.2) | — |
| [[A498 (line)]] | wt | 1.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +9.9) | — |
| [[A549 (line)]] | wt | 2.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 2.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.2× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 1.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 2.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 89.3× (z +14.5) | — |
| [[HEC-1-A (line)]] | alt | 2.55 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.7× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.4× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 2.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +13.3) | — |
| [[Hs 766T (line)]] | wt | 2.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +10.2) | — |
| [[KATO III (line)]] | alt | 3.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 2.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 1.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 16.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.0× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 1.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +8.9) | — |
| [[A-427 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02307]] | +0.86 | +0.89 / +0.66 | both halves | 7e-06 |  |
| [[NEB]] | +0.79 | +0.80 / +0.52 | both halves | 1e-05 |  |
| [[GUCY2C-AS1]] | +0.75 | +0.73 / +0.46 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | +0.75 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[LINC00486]] | +0.75 | +0.77 / +0.49 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.74 | +0.78 / +0.34 | both halves | 1e-04 |  |
| [[LINC00240]] | +0.74 | +0.77 / +0.41 | both halves | 4e-05 |  |
| [[RBM26-AS1]] | +0.74 | +0.76 / +0.36 | both halves | 1e-04 |  |
| [[LINC01090]] | +0.73 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | +0.73 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[MMADHC-DT]] | +0.73 | +0.71 / +0.40 | both halves | 5e-05 |  |
| [[NANOS3]] | +0.72 | +0.72 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D24]] | -0.71 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.68 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[WASF3]] | -0.68 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[GTPBP3]] | -0.67 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ATP7B]] | -0.67 | -0.66 / -0.38 | both halves | 7e-05 |  |
| [[ACTR5]] | -0.66 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[METAP1]] | -0.66 | -0.70 / -0.34 | both halves | 1e-04 |  |
| [[CBX1]] | -0.65 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[RPA1]] | -0.65 | -0.69 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB34]] | B | RAB34 activity lowers ANGPT2's level | lines that do not express RAB34 (16) vs lines expressing it (34) | 1.20× higher at baseline in the lines without RAB34 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RNF150, PYGO1 |
| [[HDAC6]] | B | HDAC6 activity raises ANGPT2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02492]] | B | LINC02492 activity raises ANGPT2's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 1.31× lower at baseline in the lines without LINC02492 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent |
| [[SPHK1]] | B | SPHK1 activity lowers ANGPT2's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.31× higher at baseline in the lines without SPHK1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, 16.0); signed map (26.4, 3.1). **Vector** length 62.3, 8.59% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +27.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +1.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | angiopoietin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:6,499,632-6,563,409 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ang2 |
| Gene groups (HGNC) | Receptor ligands; Fibrinogen C domain containing; Angiopoietins |
| Reactome | 3 pathways, smallest: Tie2 Signaling; Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [O15123](https://www.uniprot.org/uniprotkb/O15123) (Angiopoietin-2):

> Binds to TEK/TIE2, competing for the ANGPT1 binding site, and modulating ANGPT1 signaling. Can induce tyrosine phosphorylation of TEK/TIE2 in the absence of ANGPT1. In the absence of angiogenic inducers, such as VEGF, ANGPT2-mediated loosening of cell-matrix contacts may induce endothelial cell apoptosis with consequent vascular regression. In concert with VEGF, it may facilitate endothelial cell migration and proliferation, thus serving as a permissive angiogenic signal. Involved in the …

**Summary**, from NCBI Gene [285](https://www.ncbi.nlm.nih.gov/gene/285):

> This gene belongs to the angiopoietin family of growth factors. The protein encoded by this gene is an antagonist of angiopoietin 1, and both angiopoietin 1 and angiopoietin 2 are ligands for the endothelial TEK receptor tyrosine kinase. Angiopoietin 2 is upregulated in multiple inflammatory diseases and is implicated in the direct control of inflammation-related signaling pathways. The encoded protein affects angiogenesis during embryogenesis and tumorigenesis, disrupts the vascular remodeling …

**Accessions** — [HGNC:485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:485) · Entrez [285](https://www.ncbi.nlm.nih.gov/gene/285) · UniProt [O15123](https://www.uniprot.org/uniprotkb/O15123) · Ensembl [ENSG00000091879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091879)

## Data

Gene col 1679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1679); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1679]; `tensor/DDL_lfc|DDL_z.npy` [1679]; `embed/gene_vectors.npy` [1679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1679 or target_col == 1679). Every well: [[ANGPT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANGPT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
