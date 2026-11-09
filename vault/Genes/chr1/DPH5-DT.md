---
symbol: "DPH5-DT"
type: "gene"
col: 13892
ensembl_id: "ENSG00000233184"
name: "DPH5 divergent transcript"
location: "1p21.2"
module: 124
arm: "+"
pooled_cpm: 8.39
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# DPH5-DT

*DPH5 divergent transcript* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +7.6, q 2e-11, up in 28 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0743×, KATO III 0.119×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 0.173×, PANC-1 0.239×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C-33 A 0.0486×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (A-172 0.0502×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.139×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFX3-DT]] (+0.76, fdr 1e-05), [[AVEN]] (+0.76, fdr 1e-05), [[ENOX2]] (+0.75, fdr 1e-05); moves opposite to [[ARL3]] (-0.74, fdr 1e-05), [[RAB3A]] (-0.73, fdr 3e-05), [[ALAD]] (-0.69, fdr 1e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC17A7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +7.6 | 2e-11 | 28/44 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +7.1 | 3e-10 | 29/42 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +6.9 | 1e-09 | 24/45 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +6.7 | 3e-09 | 25/43 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.64×** | +6.7 | 3e-09 | 28/47 (Hs 766T, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +6.1 | 8e-08 | 29/46 (HT-29, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.73×** | +5.1 | 3e-05 | 18/34 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.72×** | +5.0 | 4e-05 | 21/45 (RKO, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 18/45 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.51×** | +3.6 | 0.016 | 8/43 (RPMI-7951, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.023 | 17/48 (HOP62, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.038 | 18/46 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.038 | 13/46 (PANC-1, A498, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.0 | 0.093 | 10/47 (NCI-H2347, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13892.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0743×, KATO III 0.119×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 0.173×, PANC-1 0.239×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C-33 A 0.0486×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (A-172 0.0502×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.139×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.690× | -3.6 | 0.21 | 12/47 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 0.689× | -3.3 | 0.28 | 10/46 (BT-474, LS 180, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.535× | -3.1 | 0.28 | 13/39 (RKO, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | 0.716× | -3.1 | 0.28 | 10/47 (AN3 CA, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Allopurinol (drug)]] 0.05 µM |  | 0.729× | -3.0 | 0.28 | 8/48 (NCI-H661, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 12.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0743× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[A-172 (line)]] | wt | 3.91 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0502× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 4.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0486× (z -11.6) |
| [[LoVo (line)]] | wt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 4.21 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0739× (z -8.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -9.2) |
| [[SW1417 (line)]] | alt | 4.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0516× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3-DT]] | +0.76 | +0.79 / +0.50 | both halves | 1e-05 | same gene group |
| [[AVEN]] | +0.76 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[ENOX2]] | +0.75 | +0.82 / +0.51 | both halves | 1e-05 |  |
| [[ST7L]] | +0.75 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.75 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.75 | +0.81 / +0.37 | both halves | 7e-05 |  |
| [[MCPH1]] | +0.74 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[DNAJC11]] | +0.73 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[ADCK1]] | +0.72 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[GABPB1-AS1]] | +0.72 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[KICS2]] | +0.72 | +0.79 / +0.47 | both halves | 2e-05 |  |
| [[SLC16A1-AS1]] | +0.71 | +0.71 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | -0.74 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.73 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ALAD]] | -0.69 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.69 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CARHSP1]] | -0.69 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[FBXO33]] | -0.69 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ABCB9]] | -0.69 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[PLEKHH3]] | -0.68 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[AHDC1]] | -0.68 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[MOSPD3]] | -0.67 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[CDON]] | -0.67 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[GNAI2]] | -0.67 | -0.66 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC17A7]] | B | SLC17A7 activity raises DPH5-DT's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without SLC17A7 | 0.015 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DPH5-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PYDC2-AS1]] | B | PYDC2-AS1 activity raises DPH5-DT's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.42× lower at baseline in the lines without PYDC2-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[PLEKHH2]] | B | PLEKHH2 activity raises DPH5-DT's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.19× lower at baseline in the lines without PLEKHH2 | 0.075 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[NXPH4]] | B | NXPH4 activity raises DPH5-DT's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.32× lower at baseline in the lines without NXPH4 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.834). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.3, -7.5); signed map (22.5, -28.1). **Vector** length 86.1, 17.1% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -3.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | DPH5 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p21.2 — chr1:101,025,844-101,090,513 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53720) · Entrez [102606465](https://www.ncbi.nlm.nih.gov/gene/102606465) · Ensembl [ENSG00000233184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233184)

## Data

Gene col 13892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13892); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13892]; `tensor/DDL_lfc|DDL_z.npy` [13892]; `embed/gene_vectors.npy` [13892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13892 or target_col == 13892). Every well: [[DPH5-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH5-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
