---
symbol: "RBM45"
type: "gene"
col: 7908
ensembl_id: "ENSG00000155636"
name: "RNA binding motif protein 45"
location: "2q31.2"
module: 1
arm: "+"
pooled_cpm: 6.82
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RBM45

*RNA binding motif protein 45* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.20× (z +8.3, q 8e-14, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.362× (z -10.7, q 5e-24, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGGT1B]] (+0.67, fdr 7e-06), [[EHHADH]] (+0.65, fdr 7e-06), [[NDUFAF5]] (+0.65, fdr 3e-05); moves opposite to [[INTS6L]] (-0.58, fdr 1e-05), [[KLHL15]] (-0.54, fdr 5e-05), [[FOSB]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KHDC1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +8.3 | 8e-14 | 39/47 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +6.7 | 7e-09 | 26/33 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +6.6 | 8e-09 | 30/47 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.52×** | +6.2 | 7e-08 | 19/46 (SW480, RKO, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +6.2 | 7e-08 | 28/47 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +5.7 | 1e-06 | 17/46 (SW480, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +5.5 | 3e-06 | 9/19 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +5.2 | 2e-05 | 24/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.5 | 4e-04 | 3/13 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.3 | 8e-04 | 16/47 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +4.0 | 0.003 | 3/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.005 | 14/46 (A549, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.013 | 12/45 (SW480, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.3 | 0.034 | 11/27 (SW1417, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.040 | 6/46 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.055 | 9/46 (A-427, AN3 CA, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.061 | 14/39 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.071 | 6/43 (A549, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.362×** | -10.7 | 5e-24 | 40/47 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.480×** | -7.7 | 3e-12 | 23/39 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.469×** | -6.3 | 6e-08 | 24/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.488×** | -6.0 | 3e-07 | 20/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.692×** | -3.6 | 0.030 | 14/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.100× (z -14.1) |
| [[J82 (line)]] | alt | 4.35 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0254× (z -13.6) |
| [[PANC-1 (line)]] | alt | 7.57 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0868× (z -13.6) |
| [[SW480 (line)]] | alt | 9.61 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -9.4) |
| [[LS 180 (line)]] | wt | 6.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGGT1B]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[EHHADH]] | +0.65 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.65 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[ZNF613]] | +0.64 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[C5orf63]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[AIMP2]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ECHDC3]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[COG2]] | +0.60 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[MRPL16]] | +0.60 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[QDPR]] | +0.60 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[HARS2]] | +0.60 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[ALKBH3]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6L]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[KLHL15]] | -0.54 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[FOSB]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TESK2]] | -0.51 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[LINC02649]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KHDC1-AS1]] | B | KHDC1-AS1 activity raises RBM45's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without KHDC1-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.0, 0.9); signed map (-5.1, -34.0). **Vector** length 56.8, 8.41% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.7 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -10.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -7.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:178,112,424-178,139,011 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRB1, FLJ44612 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUH3](https://www.uniprot.org/uniprotkb/Q8IUH3) (RNA-binding protein 45):

> RNA-binding protein with binding specificity for poly(C). May play an important role in neural development.

**Summary**, from NCBI Gene [129831](https://www.ncbi.nlm.nih.gov/gene/129831):

> This gene encodes a member of the RNA recognition motif (RRM)-type RNA-binding family of proteins. This protein exhibits preferential binding to poly(C) RNA. Initial cloning of this gene found that the rat ortholog was dynamically expressed in the developing rat brain. This protein has been localized to inclusion bodies in the brain and spinal cord of amyotrophic lateral sclerosis and Alzheimer's patients. A pseudogene has been identified on chromosome 8. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:24468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24468) · Entrez [129831](https://www.ncbi.nlm.nih.gov/gene/129831) · UniProt [Q8IUH3](https://www.uniprot.org/uniprotkb/Q8IUH3) · Ensembl [ENSG00000155636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155636)

## Data

Gene col 7908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7908); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7908]; `tensor/DDL_lfc|DDL_z.npy` [7908]; `embed/gene_vectors.npy` [7908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7908 or target_col == 7908). Every well: [[RBM45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
