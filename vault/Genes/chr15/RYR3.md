---
symbol: "RYR3"
type: "gene"
col: 12701
ensembl_id: "ENSG00000198838"
name: "ryanodine receptor 3"
location: "15q13.3-q14"
module: 165
arm: "+"
pooled_cpm: 6.86
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# RYR3

*ryanodine receptor 3* — 15q13.3-q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 11.6× (z +30.6, q 0e+00, up in 20 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.19× (z +20.4, q 0e+00, up in 29 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H23 0.0898×; ⚠ cell-cycle shift, explains ~27% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.491×; ⚠ position not correctable); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H23 0.0880×); [[Binimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.126×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.122×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP2]] (+0.78, fdr 7e-06), [[MTUS2]] (+0.76, fdr 1e-05), [[DPP6]] (+0.76, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **11.6×** | +30.6 | 0e+00 | 20/22 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.6×** | +28.9 | 0e+00 | 6/9 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **10.6×** | +22.3 | 0e+00 | 9/12 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.19×** | +20.4 | 0e+00 | 29/37 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +20.3 | 0e+00 | 30/36 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.78×** | +18.0 | 0e+00 | 36/44 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.90×** | +12.6 | 3e-34 | 25/41 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.27×** | +10.2 | 1e-22 | 25/42 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +8.5 | 1e-15 | 22/40 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +7.8 | 4e-13 | 20/34 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.4 | 9e-12 | 13/34 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +7.1 | 5e-11 | 17/43 (RPMI-7951, NCI-H460, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +6.5 | 4e-09 | 11/31 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +6.3 | 1e-08 | 9/26 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.41×** | +5.7 | 4e-07 | 5/17 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +5.6 | 7e-07 | 13/43 (CFPAC-1, C32, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.4 | 3e-06 | 11/42 (C32, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.9 | 3e-05 | 13/45 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.3 | 6e-04 | 11/46 (LOX-IMVI, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +4.2 | 7e-04 | 6/43 (SW1417, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.004 | 2/37 (PANC-1, KATO III) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.011 | 10/45 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12701.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H23 0.0898×; ⚠ cell-cycle shift, explains ~27% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.491×; ⚠ position not correctable); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H23 0.0880×); [[Binimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.126×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -4.6 | 0.002 | 15/47 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.770× | -3.1 | 0.32 | 5/46 (NCI-H23, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.840× | -3.1 | 0.32 | 7/44 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.783× | -3.1 | 0.32 | 3/45 (SW48, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 112 | 0 | 8 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0898× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0880× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 3.89 | 5 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.00× (z +12.5) | — |
| [[A549 (line)]] | wt | 5.98 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.3× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 7.09× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 4.09 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.9× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 2.43 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 34.4× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 10.8× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 6.68 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 32.2× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 9.69 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.67× (z +10.5) | — |
| [[SW480 (line)]] | alt | 2.31 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.88× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +8.7) | — |
| [[A-172 (line)]] | wt | 3.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +10.9) | — |
| [[A-427 (line)]] | wt | 2.34 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.1× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 54.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 4.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 3.28 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 27.6× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 2.22 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 35.9× (z +8.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 2.96 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 39.7× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 3.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 2.42 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 45.3× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 5.79 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.85× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 2.16 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 53.2× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 6.58 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.6× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP2]] | +0.78 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.76 | +0.55 / +0.82 | both halves | 1e-05 |  |
| [[DPP6]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[COL23A1]] | +0.73 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.72 | +0.51 / +0.79 | both halves | 1e-05 |  |
| [[RELN]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[RBFOX3]] | +0.71 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.71 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[CNTNAP5]] | +0.71 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[USH2A]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[LINC01579]] | +0.70 | +0.57 / +0.64 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RYR3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.8, 31.0); signed map (30.6, 16.9). **Vector** length 65.2, 10.0% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +30.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +28.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +22.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +20.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +1.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | ryanodine receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3-q14 — chr15:33,310,962-33,866,121 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ryanodine receptors; EF-hand domain containing |
| Reactome | 6 pathways, smallest: Ion homeostasis; Stimuli-sensing channels; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15413](https://www.uniprot.org/uniprotkb/Q15413) (Ryanodine receptor 3):

> Cytosolic calcium-activated calcium channel that mediates the release of Ca(2+) from the sarcoplasmic reticulum into the cytoplasm in muscle and thereby plays a role in triggering muscle contraction. May regulate Ca(2+) release by other calcium channels. Calcium channel that mediates Ca(2+)-induced Ca(2+) release from the endoplasmic reticulum in non-muscle cells. Contributes to cellular calcium ion homeostasis (By similarity). Plays a role in cellular calcium signaling.

**Summary**, from NCBI Gene [6263](https://www.ncbi.nlm.nih.gov/gene/6263):

> The protein encoded by this gene is a ryanodine receptor, which functions to release calcium from intracellular storage for use in many cellular processes. For example, the encoded protein is involved in skeletal muscle contraction by releasing calcium from the sarcoplasmic reticulum followed by depolarization of T-tubules. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:10485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10485) · Entrez [6263](https://www.ncbi.nlm.nih.gov/gene/6263) · UniProt [Q15413](https://www.uniprot.org/uniprotkb/Q15413) · Ensembl [ENSG00000198838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198838)

## Data

Gene col 12701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12701); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12701]; `tensor/DDL_lfc|DDL_z.npy` [12701]; `embed/gene_vectors.npy` [12701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12701 or target_col == 12701). Every well: [[RYR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RYR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
