---
symbol: "CLDN18"
type: "gene"
col: 826
ensembl_id: "ENSG00000066405"
name: "claudin 18"
location: "3q22.3"
module: 21
arm: "+"
pooled_cpm: 2.21
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CLDN18

*claudin 18* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.78× (z +7.8, q 3e-12, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +7.2, q 2e-10, up in 6 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.462× (z -6.1, q 5e-07, down in 19 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.0448×; ⚠ cell-cycle shift, explains ~48% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.0668×); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.174×; ⚠ cell-cycle shift, explains ~10% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.212×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EOGT-DT]] (+0.70, fdr 1e-05), [[PP2D1]] (+0.68, fdr 1e-05), [[BIRC6-AS2-1]] (+0.67, fdr 1e-05); moves opposite to [[PSMG1]] (-0.65, fdr 7e-06), [[CDCA7L]] (-0.60, fdr 1e-05), [[AKAP11]] (-0.60, fdr 8e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +7.8 | 3e-12 | 2/4 (NCI-H2347, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +7.2 | 2e-10 | 6/25 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +6.8 | 2e-09 | 1/8 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +5.3 | 1e-05 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +4.8 | 2e-04 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +3.6 | 0.026 | 1/2 (KATO III) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.027 | 0/15 | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.037 | 4/14 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +3.4 | 0.037 | 0/3 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.043 | 0/23 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.3 | 0.045 | 1/11 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.075 | 1/25 (A549) | inconsistent across doses | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.1 | 0.082 | 0/15 | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.0 | 0.093 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.094 | 1/31 (A549) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.0448×; ⚠ cell-cycle shift, explains ~48% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.0668×); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.174×; ⚠ cell-cycle shift, explains ~10% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.212×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.462×** | -6.1 | 5e-07 | 19/41 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.572×** | -4.4 | 0.003 | 19/39 (KATO III, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 33.7 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0448× (z -12.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0668× (z -10.8) |
| [[A-172 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.674 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.751 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.998 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.823 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.861 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.580 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.925 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.768 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOGT-DT]] | +0.70 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[PP2D1]] | +0.68 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[BIRC6-AS2-1]] | +0.67 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[RHOQ-AS1]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[ZRANB2-AS1]] | +0.65 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[A2ML1-AS1]] | +0.64 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[FAM217A]] | +0.64 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[SLC13A4]] | +0.64 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[TICAM2-AS1]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[VPS39-DT]] | +0.63 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[TMEM165]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PROSER2-AS1]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | -0.65 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[CDCA7L]] | -0.60 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.60 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[PRKDC]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ALG10]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[MTHFD1]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[G3BP1]] | -0.57 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[ATIC]] | -0.56 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[BACE1-AS]] | -0.56 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ATP5F1A]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SSRP1]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RIF1]] | -0.55 | -0.51 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CLDN18's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 29.0); signed map (34.0, 6.3). **Vector** length 31.1, 3.02% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +0.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.1 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | claudin 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:137,998,735-138,033,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SFTPJ |
| Gene groups (HGNC) | Claudins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P56856](https://www.uniprot.org/uniprotkb/P56856) (Claudin-18):

> Involved in alveolar fluid homeostasis via regulation of alveolar epithelial tight junction composition and therefore ion transport and solute permeability, potentially via downstream regulation of the actin cytoskeleton organization and beta-2-adrenergic signaling (By similarity). Required for lung alveolarization and maintenance of the paracellular alveolar epithelial barrier (By similarity). Acts to maintain epithelial progenitor cell proliferation and organ size, via regulation of YAP1 …

**Summary**, from NCBI Gene [51208](https://www.ncbi.nlm.nih.gov/gene/51208):

> This gene encodes a member of the claudin family. Claudins are integral membrane proteins and components of tight junction strands. Tight junction strands serve as a physical barrier to prevent solutes and water from passing freely through the paracellular space between epithelial or endothelial cell sheets, and also play critical roles in maintaining cell polarity and signal transductions. This gene is upregulated in patients with ulcerative colitis and highly overexpressed in infiltrating …

**Accessions** — [HGNC:2039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2039) · Entrez [51208](https://www.ncbi.nlm.nih.gov/gene/51208) · UniProt [P56856](https://www.uniprot.org/uniprotkb/P56856) · Ensembl [ENSG00000066405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066405)

## Data

Gene col 826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 826); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 826]; `tensor/DDL_lfc|DDL_z.npy` [826]; `embed/gene_vectors.npy` [826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 826 or target_col == 826). Every well: [[CLDN18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
