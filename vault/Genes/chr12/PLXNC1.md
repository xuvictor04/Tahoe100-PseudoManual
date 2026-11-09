---
symbol: "PLXNC1"
type: "gene"
col: 5802
ensembl_id: "ENSG00000136040"
name: "plexin C1"
location: "12q22"
module: 75
arm: "+"
pooled_cpm: 3.08
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# PLXNC1

*plexin C1* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +13.7, q 1e-39, up in 22 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0294×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (A-172 0.0654×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.127×; ⚠ cell-cycle shift, explains ~23% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.193×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THSD7B]] (+0.73, fdr 7e-06), [[SLC9C1]] (+0.73, fdr 7e-06), [[LINC01933]] (+0.71, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +13.7 | 1e-39 | 22/33 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +13.5 | 4e-39 | 2/5 (HepG2/C3A, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +11.8 | 1e-29 | 27/46 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +11.3 | 2e-27 | 7/14 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +10.8 | 3e-25 | 19/33 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +9.1 | 1e-17 | 20/40 (HOP62, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.6 | 3e-09 | 2/7 (HepG2/C3A, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.0 | 2e-07 | 13/29 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.4 | 4e-06 | 9/32 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.4 | 4e-06 | 9/46 (LoVo, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.3 | 5e-06 | 11/41 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.1 | 1e-05 | 13/37 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +4.7 | 1e-04 | 8/34 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.6 | 2e-04 | 8/35 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.4 | 3e-04 | 4/20 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +4.3 | 7e-04 | 10/40 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.008 | 10/43 (LoVo, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.063 | 1/28 (MIA PaCa-2) | inconsistent across doses |  |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.070 | 4/34 (RPMI-7951, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5802.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0294×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (A-172 0.0654×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.127×; ⚠ cell-cycle shift, explains ~23% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.827× | -3.2 | 0.48 | 6/46 (SK-MEL-2, SW 1088, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.2 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +14.0) | [[Digitoxin (drug)]] 5 µM 0.0294× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.193× (z -9.2) |
| [[A-172 (line)]] | wt | 7.88 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0654× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 3.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +9.2) | — |
| [[A-427 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD7B]] | +0.73 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.73 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[LINC01933]] | +0.71 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[DPP6]] | +0.69 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ESR1]] | +0.69 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[GRM8]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CFAP20DC-DT]] | +0.66 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SP140]] | +0.66 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.66 | +0.57 / +0.69 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLXNC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF385B]] | B | ZNF385B activity raises PLXNC1's level | lines that do not express ZNF385B (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without ZNF385B | 0.040 | ⚠ within organs, on part of the lines; also absent: DTNA, CFI, CYGB; maybe low, not absent |
| [[ANOS2P]] | B | ANOS2P activity raises PLXNC1's level | lines that do not express ANOS2P (32) vs lines expressing it (18) | 1.50× lower at baseline in the lines without ANOS2P | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, KDM5D |
| [[KCND3]] | B | KCND3 activity raises PLXNC1's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without KCND3 | 0.090 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.6, 27.3); signed map (31.8, 14.1). **Vector** length 50.2, 5.76% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | +1.2 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | plexin C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:94,148,577-94,307,675 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VESPR, CD232 |
| Gene groups (HGNC) | CD molecules; Plexins; IPT domain containing |
| Reactome | 4 pathways, smallest: Other semaphorin interactions; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O60486](https://www.uniprot.org/uniprotkb/O60486) (Plexin-C1):

> Receptor for SEMA7A, for smallpox semaphorin A39R, vaccinia virus semaphorin A39R and for herpesvirus Sema protein. Binding of semaphorins triggers cellular responses leading to the rearrangement of the cytoskeleton and to secretion of IL6 and IL8 (By similarity).

**Summary**, from NCBI Gene [10154](https://www.ncbi.nlm.nih.gov/gene/10154):

> This gene encodes a member of the plexin family. Plexins are transmembrane receptors for semaphorins, a large family of proteins that regulate axon guidance, cell motility and migration, and the immune response. The encoded protein and its ligand regulate melanocyte adhesion, and viral semaphorins may modulate the immune response by binding to this receptor. The encoded protein may be a tumor suppressor protein for melanoma. Alternatively spliced transcript variants have been observed for this …

**Accessions** — [HGNC:9106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9106) · Entrez [10154](https://www.ncbi.nlm.nih.gov/gene/10154) · UniProt [O60486](https://www.uniprot.org/uniprotkb/O60486) · Ensembl [ENSG00000136040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136040)

## Data

Gene col 5802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5802); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5802]; `tensor/DDL_lfc|DDL_z.npy` [5802]; `embed/gene_vectors.npy` [5802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5802 or target_col == 5802). Every well: [[PLXNC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
