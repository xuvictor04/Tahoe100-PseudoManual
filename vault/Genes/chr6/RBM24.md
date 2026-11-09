---
symbol: "RBM24"
type: "gene"
col: 3332
ensembl_id: "ENSG00000112183"
name: "RNA binding motif protein 24"
location: "6p22.3"
module: 66
arm: "+"
pooled_cpm: 2.69
n_lines_expressing: 27
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# RBM24

*RNA binding motif protein 24* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.31× (z +16.3, q 0e+00, up in 10 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.04× (z +12.9, q 9e-36, up in 11 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0745×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF2]] (+0.63, fdr 1e-05), [[CFL2]] (+0.63, fdr 1e-05), [[COL12A1]] (+0.63, fdr 1e-05); moves opposite to [[SFI1]] (-0.57, fdr 5e-05), [[CLTCL1]] (-0.53, fdr 4e-05), [[DRD4]] (-0.52, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[MRAS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.31×** | +16.3 | 0e+00 | 10/12 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.04×** | +12.9 | 9e-36 | 11/18 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.84×** | +12.5 | 2e-33 | 3/3 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.25×** | +11.0 | 6e-26 | 4/5 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +9.5 | 2e-19 | 11/16 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +7.5 | 6e-12 | 9/17 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +7.4 | 9e-12 | 10/24 (SNU-423, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +7.0 | 2e-10 | 9/19 (HOP62, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +6.7 | 1e-09 | 10/17 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +6.7 | 2e-09 | 9/12 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +5.5 | 2e-06 | 7/20 (A-172, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +5.3 | 6e-06 | 12/23 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +5.1 | 2e-05 | 12/24 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.16×** | +4.9 | 3e-05 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.14×** | +4.9 | 3e-05 | 3/7 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +4.5 | 3e-04 | 6/21 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +4.4 | 4e-04 | 6/24 (HOP62, J82, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.92×** | +3.8 | 0.004 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.38×** | +3.7 | 0.005 | 9/21 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.008 | 9/24 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.017 | 3/17 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | **1.47×** | +3.1 | 0.037 | 0/19 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3332.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0745×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -3.2 | 0.89 | 6/24 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.2) | — |
| [[A549 (line)]] | wt | 7.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0745× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 6.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +13.7) | — |
| [[A-172 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.206 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.731 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.439 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF2]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CFL2]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[COL12A1]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TAF9B]] | +0.61 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[DMD]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[RARG]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FAT3]] | +0.58 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[GFRA1]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[GUCY1A2]] | +0.57 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[CAV2]] | +0.57 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[MAPK10]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[MAGI2-AS3]] | +0.56 | +0.39 / +0.49 | both halves | 6e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFI1]] | -0.57 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[CLTCL1]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[DRD4]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[OGG1]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[LCMT1]] | -0.51 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[WRN]] | -0.51 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[SMYD4]] | -0.51 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CNOT10]] | -0.51 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[ZXDC]] | -0.50 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ANKS3]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[EIF3K]] | -0.49 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[PPP2R3B]] | -0.49 | -0.53 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRAS]] | B | RBM24 activity raises MRAS's level | lines that do not express RBM24 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without RBM24 | 0.062 | ⚠ within organs, on part of the lines; also absent: SRGN, P3H2, FMN2 |
| [[ANKS3]] | B | RBM24 activity strengthens ANKS3's drug response | lines that do not express RBM24 (23) vs lines expressing it (25) | the lines without RBM24 respond 0.75× as strongly (z diff +1.06); strongest at Dinaciclib 5 µM: 0.72x vs 0.41x (z diff +3.7) | 0.068 | ⚠ within organs, on part of the lines; also absent: SRGN, P3H2, FMN2; target measured in part of the lines; artifact flags |
| [[FGF2]] | C | RBM24 activity raises FGF2's level | lines that do not express RBM24 (23) vs lines expressing it (27) | 2.83× lower at baseline in the lines without RBM24 | 0.010 | ⚠ within organs, on part of the lines; also absent: SRGN, P3H2, FMN2; co-absent with the target |
| [[TRIM58]] | C | RBM24 activity raises TRIM58's level | lines that do not express RBM24 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without RBM24 | 0.026 | ⚠ within organs, on part of the lines; also absent: SRGN, P3H2, FMN2; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.2, 21.4); signed map (43.9, 19.4). **Vector** length 40.0, 7.50% of its response variance represented; |z| ≥ 3 in 508 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -0.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:17,281,361-17,293,871 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30829, dJ259A10.1; previously RNPC6 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX46](https://www.uniprot.org/uniprotkb/Q9BX46) (RNA-binding protein 24):

> Multifunctional RNA-binding protein involved in the regulation of pre-mRNA splicing, mRNA stability and mRNA translation important for cell fate decision and differentiation. Plays a major role in pre-mRNA alternative splicing regulation. Mediates preferentially muscle-specific exon inclusion in numerous mRNAs important for striated cardiac and skeletal muscle cell differentiation. Binds to intronic splicing enhancer (ISE) composed of stretches of GU-rich motifs localized in flanking intron of …

**Summary**, from NCBI Gene [221662](https://www.ncbi.nlm.nih.gov/gene/221662):

> Enables mRNA 3'-UTR AU-rich region binding activity; mRNA CDS binding activity; and sequence-specific mRNA binding activity. Involved in several processes, including negative regulation of cytoplasmic translation; positive regulation of cell differentiation; and regulation of mRNA metabolic process. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21539) · Entrez [221662](https://www.ncbi.nlm.nih.gov/gene/221662) · UniProt [Q9BX46](https://www.uniprot.org/uniprotkb/Q9BX46) · Ensembl [ENSG00000112183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112183)

## Data

Gene col 3332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3332); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3332]; `tensor/DDL_lfc|DDL_z.npy` [3332]; `embed/gene_vectors.npy` [3332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3332 or target_col == 3332). Every well: [[RBM24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
