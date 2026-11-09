---
symbol: "HAL"
type: "gene"
col: 1395
ensembl_id: "ENSG00000084110"
name: "histidine ammonia-lyase"
location: "12q23.1"
module: 47
arm: "+"
pooled_cpm: 3.06
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# HAL

*histidine ammonia-lyase* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.23× (z +11.3, q 5e-27, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.675× (z -3.8, q 0.051, down in 14 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02725]] (+0.57, fdr 1e-05), [[BMP8A]] (+0.55, fdr 2e-05), [[ADGRE2]] (+0.54, fdr 4e-05); moves opposite to [[NIPSNAP3A]] (-0.51, fdr 4e-05), [[PI4K2B]] (-0.45, fdr 2e-04), [[CNOT9]] (-0.41, fdr 1e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GSDMC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.23×** | +11.3 | 5e-27 | 39/45 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.97×** | +10.5 | 2e-23 | 35/44 (NCI-H2030, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +9.9 | 5e-21 | 17/34 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +8.7 | 4e-16 | 25/44 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.7 | 5e-16 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.2 | 8e-11 | 21/43 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +5.6 | 2e-06 | 14/44 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.44×** | +5.0 | 4e-05 | 13/31 (LoVo, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 9e-05 | 13/31 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 1e-04 | 11/35 (Panc 03.27, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.41×** | +4.7 | 1e-04 | 9/43 (NCI-H460, HCT15, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 4/44 (A549, C-33 A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +3.7 | 0.011 | 2/44 (HEC-1-A, LoVo) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.48×** | +3.5 | 0.018 | 0/5 | all doses, stronger at high dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.021 | 9/40 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.048 | 4/25 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.048 | 4/24 (NCI-H2030, HCT15, …) | rises with dose | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.048 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -3.8 | 0.051 | 14/40 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.683×** | -3.7 | 0.051 | 4/39 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -3.6 | 0.051 | 13/24 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | **0.776×** | -3.5 | 0.073 | 8/38 (HT-29, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.707×** | -3.4 | 0.076 | 14/42 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Erlotinib (drug)]] 5 µM |  | **0.697×** | -3.4 | 0.076 | 12/37 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.717×** | -3.2 | 0.094 | 8/39 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -3.2 | 0.094 | 7/37 (MIA PaCa-2, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.701×** | -3.2 | 0.096 | 11/43 (NCI-H460, COLO 205, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.30 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0796× (z -10.8) ⚠ transcription drop; cell-cycle shift, explains ~83% of this change |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0362× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 3.37 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0664× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0886× (z -8.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 3.51 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0641× (z -9.7) |
| [[PANC-1 (line)]] | alt | 1.22 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0507× (z -8.7) |
| [[SW480 (line)]] | alt | 2.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +9.0) | — |
| [[A-172 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02725]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[BMP8A]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ADGRE2]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[A3GALT2]] | +0.54 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[ATF1]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[CFAP251]] | +0.53 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[CPNE9]] | +0.52 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[PYGM]] | +0.50 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SKI]] | +0.50 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[TREM1]] | +0.49 | +0.27 / +0.48 | both halves | 3e-04 |  |
| [[FNDC7]] | +0.49 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[KCNMB4]] | +0.48 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPSNAP3A]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PI4K2B]] | -0.45 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[CNOT9]] | -0.41 | -0.43 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSDMC]] | B | GSDMC activity raises HAL's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 1.94× lower at baseline in the lines without GSDMC | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[ADGRE2]] | B | ADGRE2 activity raises HAL's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without ADGRE2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.2, -14.9); signed map (15.3, 16.9). **Vector** length 55.7, 7.38% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +8.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.6 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.2 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | histidine ammonia-lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:95,972,662-95,996,365 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HIS |
| Gene groups (HGNC) | Carbon-nitrogen lyases |
| Reactome | 2 pathways, smallest: Histidine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P42357](https://www.uniprot.org/uniprotkb/P42357) (Histidine ammonia-lyase):

> Catalyzes the first reaction in histidine catabolism, the non-oxidative deamination of L-histidine to trans-urocanic.

**Summary**, from NCBI Gene [3034](https://www.ncbi.nlm.nih.gov/gene/3034):

> Histidine ammonia-lyase is a cytosolic enzyme catalyzing the first reaction in histidine catabolism, the nonoxidative deamination of L-histidine to trans-urocanic acid. Histidine ammonia-lyase defects cause histidinemia which is characterized by increased histidine and histamine and decreased urocanic acid in body fluids. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:4806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4806) · Entrez [3034](https://www.ncbi.nlm.nih.gov/gene/3034) · UniProt [P42357](https://www.uniprot.org/uniprotkb/P42357) · Ensembl [ENSG00000084110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084110)

## Data

Gene col 1395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1395); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1395]; `tensor/DDL_lfc|DDL_z.npy` [1395]; `embed/gene_vectors.npy` [1395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1395 or target_col == 1395). Every well: [[HAL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
