---
symbol: "PTCH2"
type: "gene"
col: 3907
ensembl_id: "ENSG00000117425"
name: "patched 2"
location: "1p34.1"
module: 47
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# PTCH2

*patched 2* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.44× (z +17.1, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Gemfibrozil (drug)]] 0.5 µM: 0.644× (z -4.4, q 0.005, down in 9 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO15A]] (+0.76, fdr 7e-06), [[CPNE9]] (+0.69, fdr 7e-06), [[BMP8A]] (+0.69, fdr 1e-05); moves opposite to [[CIAO2A]] (-0.54, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC00334]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.44×** | +17.1 | 0e+00 | 45/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.66×** | +13.1 | 1e-36 | 42/45 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +12.3 | 2e-32 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +12.0 | 6e-31 | 26/36 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.13×** | +11.5 | 1e-28 | 40/45 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +10.7 | 2e-24 | 7/11 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +9.7 | 3e-20 | 16/32 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +7.1 | 9e-11 | 2/5 (HOP62, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.7 | 2e-09 | 13/34 (A549, HCT15, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +5.8 | 3e-07 | 15/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.3 | 8e-06 | 12/45 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +4.7 | 1e-04 | 8/41 (LoVo, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.3 | 7e-04 | 9/23 (RKO, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.54×** | +4.2 | 0.001 | 1/13 (NCI-H460) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.003 | 3/16 (MIA PaCa-2, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.006 | 5/19 (SW480, PANC-1, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.007 | 4/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.038 | 1/20 (LoVo) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.090 | 1/46 (A498) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gemfibrozil (drug)]] 0.5 µM |  | **0.644×** | -4.4 | 0.005 | 9/42 (HT-29, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.681×** | -3.9 | 0.028 | 12/46 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -3.5 | 0.074 | 9/45 (HEC-1-A, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.548× | -3.2 | 0.18 | 5/39 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.732× | -3.2 | 0.18 | 13/44 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.24 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0892× (z -9.1) |
| [[SW480 (line)]] | alt | 3.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +8.5) | — |
| [[A-172 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO15A]] | +0.76 | +0.78 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CPNE9]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[BMP8A]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SGSM3-AS1]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[KIF17]] | +0.66 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[CHRNA10]] | +0.65 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[HPX]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[NTRK1]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MSANTD1]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ATP8B5P-1]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SH2D4B]] | +0.62 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[TMEM25]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2A]] | -0.54 | -0.58 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00334]] | B | LINC00334 activity raises PTCH2's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without LINC00334 | 0.003 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises PTCH2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without ASGR1 | 0.029 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[SSC5D]] | B | SSC5D activity raises PTCH2's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without SSC5D | 0.061 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[CCDC144CP]] | B | CCDC144CP activity raises PTCH2's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without CCDC144CP | 0.077 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[KIF17]] | C | KIF17 activity raises PTCH2's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without KIF17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent; its own permutation p |
| [[AXDND1]] | C | AXDND1 activity raises PTCH2's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without AXDND1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.3, -15.1); signed map (16.6, 15.1). **Vector** length 42.9, 4.19% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +17.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | patched 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,819,844-44,843,253 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLC65B2 |
| Gene groups (HGNC) | Solute carrier family 65 |
| Reactome | 6 pathways, smallest: GLI proteins bind promoters of Hh responsive genes to promote transcription; Class B/2 (Secretin family receptors); Hedgehog 'on' state |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6C5](https://www.uniprot.org/uniprotkb/Q9Y6C5) (Protein patched homolog 2):

> Negative regulator of the smoothened signaling pathway, which acts as a receptor for hedgehog (SHH, IHH and DHH) morphogens. In absence of hedgehog, acts as an inhibitor of smoothened protein (SMO) by preventing SMO access to cholesterol: mechanistically, acts as a cholesterol transporter, which depeletes cholesterol from the outer leaflet of plasma membrane, thereby preventing cholesterol-binding to the extracellular CRD region of SMO. Hedgehog-binding inhibits PTCH1 cholesterol transporter …

**Summary**, from NCBI Gene [8643](https://www.ncbi.nlm.nih.gov/gene/8643):

> This gene encodes a transmembrane receptor of the patched gene family. The encoded protein may function as a tumor suppressor in the hedgehog signaling pathway. Alterations in this gene have been associated with nevoid basal cell carcinoma syndrome, basal cell carcinoma, medulloblastoma, and susceptibility to congenital macrostomia. Alternatively spliced transcript variants have been described.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:9586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9586) · Entrez [8643](https://www.ncbi.nlm.nih.gov/gene/8643) · UniProt [Q9Y6C5](https://www.uniprot.org/uniprotkb/Q9Y6C5) · Ensembl [ENSG00000117425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117425)

## Data

Gene col 3907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3907); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3907]; `tensor/DDL_lfc|DDL_z.npy` [3907]; `embed/gene_vectors.npy` [3907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3907 or target_col == 3907). Every well: [[PTCH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTCH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
