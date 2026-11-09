---
symbol: "FBXO43"
type: "gene"
col: 7991
ensembl_id: "ENSG00000156509"
name: "F-box protein 43"
location: "8q22.2"
module: 71
arm: "+"
pooled_cpm: 2.43
n_lines_expressing: 42
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# FBXO43

*F-box protein 43* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.56× (z +17.5, q 0e+00, up in 13 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.96× (z +13.2, q 8e-38, up in 22 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.627× (z -3.8, q 0.074, down in 13 of 30 measured lines) ⚠ cell-cycle shift, explains ~46% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.5 µM in 1 line (SW 1088 0.181×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 0.0622×; ⚠ cell-cycle shift, would explain all of this change); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (A498 0.0770×); [[Idarubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (A-172 0.0948×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMNB1-DT]] (+0.70, fdr 7e-06), [[TLCD3B]] (+0.68, fdr 7e-06), [[ARHGEF39]] (+0.68, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[GSK1059615 (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.56×** | +17.5 | 0e+00 | 13/14 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.14×** | +16.4 | 0e+00 | 3/3 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.93×** | +15.5 | 0e+00 | 4/4 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +13.2 | 8e-38 | 22/30 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.28×** | +10.1 | 9e-22 | 20/30 (NCI-H2030, HS-578T, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.17×** | +6.1 | 1e-07 | 9/17 (NCI-H460, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.80×** | +5.1 | 3e-05 | 2/13 (NCI-H2030, NCI-H23) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.9 | 7e-05 | 2/13 (PANC-1, Hs 766T) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.72×** | +4.7 | 2e-04 | 9/37 (A498, RKO, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.42×** | +4.2 | 0.001 | 4/35 (PANC-1, LoVo, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.2 | 0.001 | 9/23 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +4.2 | 0.001 | 6/31 (Panc 03.27, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.4 | 0.029 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.047 | 7/36 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.44×** | +3.2 | 0.060 | 4/35 (HEC-1-A, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7991.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.5 µM in 1 line (SW 1088 0.181×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 0.0622×; ⚠ cell-cycle shift, would explain all of this change); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (A498 0.0770×); [[Idarubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (A-172 0.0948×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.627×** | -3.8 | 0.074 | 13/30 (SK-MEL-2, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.780× | -3.1 | 0.63 | 8/37 (A498, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.14 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0622× (z -10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0948× (z -8.9) |
| [[A498 (line)]] | wt | 3.43 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0770× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 5.30 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +8.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SHP-77 (line)]] | alt | 9.27 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0956× (z -8.9) |
| [[SW 1088 (line)]] | alt | 1.69 | 0 | 1 | — | [[c-Kit-IN-1 (drug)]] 0.5 µM 0.181× (z -15.4) |
| [[A-427 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.810 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.786 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.685 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.887 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMNB1-DT]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[TLCD3B]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[ARHGEF39]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[REXO5]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[DMC1]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[GPR19]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PRC1]] | +0.63 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[C21orf58]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[C10orf88B]] | +0.61 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[C5]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SPDL1]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CENPH]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[GSK1059615 (drug)]] 5 µM | B | FBXO43 activity raises the cells' numbers under GSK1059615 5 µM (protects the cells) | lines that do not express FBXO43 (8) vs lines expressing it (40) | the lines without FBXO43: 0.63× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: FBXL2, SLC36A4, FERMT2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.396). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.6, -48.7); signed map (-45.6, -48.4). **Vector** length 50.0, 7.77% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +17.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.2 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | -1.7 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | +0.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:100,133,351-100,145,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Fbx43 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G163](https://www.uniprot.org/uniprotkb/Q4G163) (F-box only protein 43):

> Required to establish and maintain the arrest of oocytes at the second meiotic metaphase until fertilization. Acts by inhibiting the anaphase-promoting complex/cyclosome (APC/C) ubiquitin ligase. Probably recognizes and binds to some phosphorylated proteins and promotes their ubiquitination and degradation. Plays a vital role in modulating the ubiquitilation of CCNB1 and CDK1 during gametogenesis.

**Summary**, from NCBI Gene [286151](https://www.ncbi.nlm.nih.gov/gene/286151):

> Members of the F-box protein family, such as FBXO43, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28521) · Entrez [286151](https://www.ncbi.nlm.nih.gov/gene/286151) · UniProt [Q4G163](https://www.uniprot.org/uniprotkb/Q4G163) · Ensembl [ENSG00000156509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156509)

## Data

Gene col 7991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7991); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7991]; `tensor/DDL_lfc|DDL_z.npy` [7991]; `embed/gene_vectors.npy` [7991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7991 or target_col == 7991). Every well: [[FBXO43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
