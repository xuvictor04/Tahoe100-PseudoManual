---
symbol: "TLE6"
type: "gene"
col: 2528
ensembl_id: "ENSG00000104953"
name: "TLE family member 6, subcortical maternal complex member"
location: "19p13.3"
module: 84
arm: "+"
pooled_cpm: 4.21
n_lines_expressing: 47
n_dd_up: 2
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# TLE6

*TLE family member 6, subcortical maternal complex member* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.37× (z +4.1, q 0.021, up in 13 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.315× (z -14.8, q 0e+00, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIN1]] (+0.59, fdr 1e-05), [[ZNF215]] (+0.59, fdr 1e-05), [[ETV5]] (+0.59, fdr 1e-05); moves opposite to [[PTPRK]] (-0.59, fdr 1e-05), [[RUFY3]] (-0.58, fdr 2e-05), [[CLIP1]] (-0.56, fdr 1e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STAMBPL1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[ABCB9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.021 | 13/42 (SW 900, HT-29, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.039 | 9/37 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Quinestrol (drug)]] 5 µM |  | 1.26× | +3.0 | 0.43 | 4/42 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.315×** | -14.8 | 0e+00 | 29/35 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.227×** | -13.5 | 4e-39 | 36/43 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.322×** | -10.3 | 1e-22 | 28/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.323×** | -10.3 | 1e-22 | 31/39 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.334×** | -10.0 | 3e-21 | 28/34 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.343×** | -9.7 | 2e-20 | 30/40 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.335×** | -9.6 | 9e-20 | 30/42 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.396×** | -7.9 | 1e-13 | 25/37 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -7.8 | 5e-13 | 28/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.426×** | -7.7 | 5e-13 | 27/39 (A-172, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.583×** | -6.9 | 3e-10 | 25/41 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.486×** | -6.3 | 1e-08 | 19/25 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -6.1 | 5e-08 | 20/33 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.520×** | -5.9 | 1e-07 | 15/41 (NCI-H23, NCI-H2030, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.530×** | -5.7 | 3e-07 | 22/43 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.306×** | -5.6 | 7e-07 | 22/40 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.534×** | -5.6 | 7e-07 | 26/44 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.22 | 0 | 12 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0819× (z -11.3) |
| [[PANC-1 (line)]] | alt | 5.77 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -19.1) |
| [[C32 (line)]] | wt | 8.98 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0486× (z -16.4) |
| [[MIA PaCa-2 (line)]] | alt | 8.63 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0908× (z -13.8) |
| [[HOP62 (line)]] | alt | 5.11 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.0602× (z -11.9) |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0555× (z -12.2) |
| [[A549 (line)]] | wt | 3.45 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0359× (z -10.4) |
| [[LS 180 (line)]] | wt | 7.94 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0628× (z -11.4) |
| [[A-172 (line)]] | wt | 4.19 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0647× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 6.29 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -9.7) |
| [[HS-578T (line)]] | alt | 3.38 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0277× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0770× (z -8.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 3.69 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0354× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 8.84 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -8.5) |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0639× (z -9.8) |
| [[SNU-423 (line)]] | alt | 4.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -9.0) |
| [[A-427 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIN1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ZNF215]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ETV5]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CPNE5]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ST3GAL5]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[RGS2]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[COL13A1]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SEPTIN6]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[PPIL3]] | +0.55 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[KDM2B-DT]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[ETV1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[RUFY3]] | -0.58 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CLIP1]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[GATA2-AS1]] | -0.53 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[DCTN2]] | -0.52 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[DUSP16]] | -0.51 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[SETD7]] | -0.50 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CAPN3]] | -0.49 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[KANSL1L]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ATP11C]] | -0.48 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[ACYP2]] | -0.48 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAMBPL1]] | C | STAMBPL1's natural level strengthens TLE6's drug response | STAMBPL1's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.53; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCB9]] | C | TLE6 activity raises ABCB9's level | lines that do not express TLE6 (3) vs lines expressing it (47) | 1.47× lower at baseline in the lines without TLE6 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF675, FOXRED2, MID1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 7.6); signed map (1.9, 53.0). **Vector** length 69.9, 12.3% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.8 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -4.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | TLE family member 6, subcortical maternal complex member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,977,538-2,995,179 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14009, GRG6 |
| Gene groups (HGNC) | WD repeat domain containing; TLE family; Subcortical maternal complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H808](https://www.uniprot.org/uniprotkb/Q9H808) (Transducin-like enhancer protein 6):

> Component of the subcortical maternal complex (SCMC), a multiprotein complex that plays a key role in early embryonic development. The SCMC complex is a structural constituent of cytoplasmic lattices, which consist in fibrous structures found in the cytoplasm of oocytes and preimplantation embryos. They are required to store maternal proteins critical for embryonic development, such as ribosomal proteins, cytoskeletal tubulins and proteins controlling epigenetic reprogramming of the …

**Summary**, from NCBI Gene [79816](https://www.ncbi.nlm.nih.gov/gene/79816):

> This gene encodes a member of the Groucho/ transducin-like Enhancer of split family of transcriptional co-repressors. The encoded protein is a component of the mammalian subcortical maternal complex, which is required for preimplantation development. In mouse, knock out of this gene results in cleavage-stage embryonic arrest resulting from defective cytoplasmic F-actin meshwork formation and asymmetric cell division. In human, an allelic variant in this gene is associated with preimplantation …

**Accessions** — [HGNC:30788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30788) · Entrez [79816](https://www.ncbi.nlm.nih.gov/gene/79816) · UniProt [Q9H808](https://www.uniprot.org/uniprotkb/Q9H808) · Ensembl [ENSG00000104953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104953)

## Data

Gene col 2528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2528); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2528]; `tensor/DDL_lfc|DDL_z.npy` [2528]; `embed/gene_vectors.npy` [2528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2528 or target_col == 2528). Every well: [[TLE6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLE6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
