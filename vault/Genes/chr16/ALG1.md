---
symbol: "ALG1"
type: "gene"
col: 408
ensembl_id: "ENSG00000033011"
name: "ALG1 chitobiosyldiphosphodolichol beta-mannosyltransferase"
location: "16p13.3"
module: 64
arm: "+"
pooled_cpm: 6.41
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# ALG1

*ALG1 chitobiosyldiphosphodolichol beta-mannosyltransferase* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.19× (z +9.8, q 9e-20, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +9.6, q 2e-19, up in 25 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.771× (z -4.8, q 1e-03, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATB]] (+0.73, fdr 7e-06), [[VPS11]] (+0.68, fdr 1e-05), [[WASHC2A]] (+0.65, fdr 1e-05); moves opposite to [[ARPC1B]] (-0.53, fdr 4e-05), [[EXTL3]] (-0.52, fdr 1e-04), [[SH3BGRL3]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +9.8 | 9e-20 | 7/10 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +9.6 | 2e-19 | 25/42 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +9.0 | 4e-17 | 22/31 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +7.7 | 2e-12 | 21/48 (A498, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +7.3 | 3e-11 | 28/47 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +5.9 | 3e-07 | 19/46 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +5.8 | 6e-07 | 22/45 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 6e-06 | 22/47 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +5.0 | 3e-05 | 8/18 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.9 | 6e-05 | 13/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 2e-04 | 13/40 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +4.4 | 6e-04 | 11/44 (SW480, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.39×** | +4.1 | 0.002 | 14/34 (A498, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.017 | 9/48 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.024 | 6/47 (BT-474, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.026 | 9/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.050 | 2/46 (SW480, A-172) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.050 | 9/46 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.061 | 6/42 (NCI-H1792, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -4.8 | 1e-03 | 17/48 (A-172, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.710×** | -4.4 | 0.002 | 13/47 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.735×** | -4.0 | 0.012 | 14/45 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.769×** | -3.4 | 0.090 | 12/48 (SW480, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.776× | -3.3 | 0.11 | 7/46 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.844× | -3.1 | 0.17 | 9/48 (A498, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.789× | -3.1 | 0.17 | 16/43 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 7.16 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0902× (z -9.9) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.127× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 7.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 6.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 9.98 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +8.9) | — |
| [[RKO (line)]] | wt | 8.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATB]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[VPS11]] | +0.68 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[WASHC2A]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SLC38A7]] | +0.65 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[TCTN1]] | +0.63 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[WASHC2C]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[CUL5]] | +0.62 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[RAE1]] | +0.61 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[PGBD4]] | +0.61 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[DUS3L]] | +0.61 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[TMEM199]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[THBS4]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC1B]] | -0.53 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[EXTL3]] | -0.52 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[SH3BGRL3]] | -0.50 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[WDR44]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SH3GL3]] | -0.49 | -0.45 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | ALG1's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | ALG1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.079 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-19.6, 13.3); signed map (-9.3, -19.9). **Vector** length 50.3, 6.02% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ALG1 chitobiosyldiphosphodolichol beta-mannosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:5,033,702-5,087,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMT-1, HMAT1, CDG1K, Mat-1 |
| Gene groups (HGNC) | Glycosyl transferases group 1 domain containing |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT22](https://www.uniprot.org/uniprotkb/Q9BT22) (Chitobiosyldiphosphodolichol beta-mannosyltransferase):

> Mannosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including two GlcNAcs, nine mannoses and three …

**Summary**, from NCBI Gene [56052](https://www.ncbi.nlm.nih.gov/gene/56052):

> The enzyme encoded by this gene catalyzes the first mannosylation step in the biosynthesis of lipid-linked oligosaccharides. This gene is mutated in congenital disorder of glycosylation type Ik. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:18294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18294) · Entrez [56052](https://www.ncbi.nlm.nih.gov/gene/56052) · UniProt [Q9BT22](https://www.uniprot.org/uniprotkb/Q9BT22) · Ensembl [ENSG00000033011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033011)

## Data

Gene col 408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 408); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 408]; `tensor/DDL_lfc|DDL_z.npy` [408]; `embed/gene_vectors.npy` [408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 408 or target_col == 408). Every well: [[ALG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
