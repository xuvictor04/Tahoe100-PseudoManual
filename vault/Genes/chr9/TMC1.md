---
symbol: "TMC1"
type: "gene"
col: 9064
ensembl_id: "ENSG00000165091"
name: "transmembrane channel like 1"
location: "9q21.13"
module: 90
arm: "+"
pooled_cpm: 4.14
n_lines_expressing: 48
n_dd_up: 29
n_dd_down: 6
n_dd_up_clean: 24
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# TMC1

*transmembrane channel like 1* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.23× (z +17.2, q 0e+00, up in 26 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.576× (z -5.7, q 6e-06, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM16-AS1]] (+0.71, fdr 1e-05), [[CLVS1]] (+0.68, fdr 7e-06), [[ALDH1A2]] (+0.64, fdr 3e-05); moves opposite to [[ORC5]] (-0.54, fdr 6e-05), [[CAD]] (-0.52, fdr 3e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[DPP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +17.2 | 0e+00 | 26/33 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.32×** | +12.3 | 3e-32 | 35/41 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +12.0 | 6e-31 | 4/8 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.40×** | +9.1 | 1e-17 | 28/37 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.29×** | +8.6 | 9e-16 | 21/40 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +8.0 | 2e-13 | 8/21 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +7.8 | 5e-13 | 3/10 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.0 | 2e-10 | 14/41 (A498, SW1417, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.73×** | +5.5 | 3e-06 | 17/39 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +5.2 | 1e-05 | 14/37 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +4.8 | 8e-05 | 12/42 (Hs 766T, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 4e-04 | 13/40 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +4.4 | 6e-04 | 14/39 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +4.0 | 0.002 | 10/40 (Hs 766T, LoVo, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.006 | 6/29 (KATO III, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.007 | 10/35 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.010 | 14/42 (Hs 766T, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.010 | 4/32 (KATO III, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.576×** | -5.7 | 6e-06 | 22/44 (HCT15, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -5.5 | 1e-05 | 21/41 (LS 180, C32, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.631×** | -4.8 | 4e-04 | 16/41 (RPMI-7951, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.765×** | -3.9 | 0.013 | 12/41 (LOX-IMVI, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.720×** | -3.4 | 0.076 | 11/39 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.097 | 7/43 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.805× | -3.2 | 0.13 | 11/41 (C-33 A, NCI-H1573, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.731× | -3.1 | 0.13 | 8/38 (HS-578T, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -11.4) |
| [[BT-474 (line)]] | alt | 6.20 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 12.5× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 5.74 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0849× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.211× (z -8.8) |
| [[A498 (line)]] | wt | 3.13 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0595× (z -9.3) |
| [[A549 (line)]] | wt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0605× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 3.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.94× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 5.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.95× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0829× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 5.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +8.5) | — |
| [[KATO III (line)]] | alt | 3.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.94× (z +9.2) | — |
| [[LoVo (line)]] | wt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 1.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -8.8) |
| [[A-172 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM16-AS1]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[CLVS1]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ALDH1A2]] | +0.64 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[LINC00578]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC00298]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MIR325HG]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[LINC02208]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[LINC02889]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[DPP6]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[SLC9C1]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[LINC01483]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[GRM8]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC5]] | -0.54 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[CAD]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPP4]] | B | DPP4 activity raises TMC1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without DPP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[TOP2A]] | B | TOP2A activity lowers TMC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUOX2]] | B | DUOX2 activity raises TMC1's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without DUOX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[ADGRF4]] | B | ADGRF4 activity raises TMC1's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without ADGRF4 | 0.038 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[LINC02343]] | B | LINC02343 activity raises TMC1's level | lines that do not express LINC02343 (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without LINC02343 | 0.046 | ⚠ within organs, on part of the lines; also absent: PRAF2; maybe low, not absent |
| [[ATXN1-AS1]] | B | ATXN1-AS1 activity raises TMC1's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without ATXN1-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[ADAM28]] | B | ADAM28 activity raises TMC1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.37× lower at baseline in the lines without ADAM28 | 0.055 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TMC1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.9, 28.2); signed map (35.0, 14.7). **Vector** length 67.2, 11.3% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +17.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +12.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -4.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane channel like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:72,521,608-72,838,297 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNA36, DFNB7, DFNB11 |
| Gene groups (HGNC) | Transmembrane channel like family |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDI8](https://www.uniprot.org/uniprotkb/Q8TDI8) (Transmembrane channel-like protein 1):

> Pore-forming subunit of the mechanotransducer (MET) non-selective cation channel complex located at the tips of stereocilia of cochlear hair cells, where it mediates mechanoelectrical transduction required for hearing. The MET complex is composed of a dimeric TMC channel core containing TMC1 or TMC2 subunits and several auxiliary proteins, including LHFPL5, TMIE, CIB2/CIB3, TOMT and the tip-link protein PCDH15. The MET channel is activated by tension in the tip link extending from the side wall …

**Summary**, from NCBI Gene [117531](https://www.ncbi.nlm.nih.gov/gene/117531):

> This gene is considered a member of a gene family predicted to encode transmembrane proteins. The specific function of this gene is unknown; however, it is known to be required for normal function of cochlear hair cells. Mutations in this gene have been associated with progressive postlingual hearing loss and profound prelingual deafness. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16513) · Entrez [117531](https://www.ncbi.nlm.nih.gov/gene/117531) · UniProt [Q8TDI8](https://www.uniprot.org/uniprotkb/Q8TDI8) · Ensembl [ENSG00000165091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165091)

## Data

Gene col 9064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9064); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9064]; `tensor/DDL_lfc|DDL_z.npy` [9064]; `embed/gene_vectors.npy` [9064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9064 or target_col == 9064). Every well: [[TMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
