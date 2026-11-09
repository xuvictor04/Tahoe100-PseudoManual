---
symbol: "GRK7"
type: "gene"
col: 3526
ensembl_id: "ENSG00000114124"
name: "G protein-coupled receptor kinase 7"
location: "3q23"
module: 37
arm: "+"
pooled_cpm: 4.08
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 5
n_dd_up_clean: 27
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# GRK7

*G protein-coupled receptor kinase 7* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.92× (z +21.4, q 0e+00, up in 33 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.627× (z -5.0, q 4e-04, down in 13 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 2 lines (HS-578T 0.0673×, HEC-1-A 0.110×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HS-578T 0.100×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAAT]] (+0.77, fdr 7e-06), [[CMYA5]] (+0.77, fdr 7e-06), [[YIPF7]] (+0.77, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +21.4 | 0e+00 | 33/39 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.55×** | +14.0 | 3e-42 | 35/38 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.32×** | +13.3 | 5e-38 | 33/42 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +10.6 | 7e-24 | 26/36 (HS-578T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.68×** | +10.5 | 1e-23 | 23/42 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.93×** | +10.3 | 9e-23 | 21/44 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.04×** | +9.4 | 6e-19 | 32/42 (NCI-H460, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +9.0 | 2e-17 | 23/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +9.0 | 2e-17 | 19/34 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.98×** | +7.6 | 2e-12 | 24/46 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.58×** | +7.4 | 8e-12 | 20/35 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **3.47×** | +7.2 | 3e-11 | 22/42 (HEC-1-A, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.1 | 6e-11 | 3/6 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +6.4 | 5e-09 | 17/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.95×** | +6.3 | 1e-08 | 5/9 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.82×** | +6.2 | 1e-08 | 17/40 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +6.2 | 2e-08 | 19/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +5.6 | 9e-07 | 20/45 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3526.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 2 lines (HS-578T 0.0673×, HEC-1-A 0.110×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HS-578T 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.627×** | -5.0 | 4e-04 | 13/40 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.672×** | -4.4 | 0.002 | 13/46 (COLO 205, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.674×** | -4.4 | 0.002 | 11/46 (H4, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.721×** | -3.6 | 0.041 | 12/46 (H4, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.739×** | -3.4 | 0.090 | 5/46 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.748× | -3.1 | 0.19 | 13/44 (LoVo, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.06 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +12.0) | [[Verteporfin (drug)]] 5 µM 0.110× (z -10.1) |
| [[LoVo (line)]] | wt | 3.14 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 7.58 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.0673× (z -10.2) |
| [[LS 180 (line)]] | wt | 4.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 3.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +8.8) | — |
| [[SW48 (line)]] | wt | 9.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +9.7) | — |
| [[SW480 (line)]] | alt | 3.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +11.5) | — |
| [[A-172 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAAT]] | +0.77 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[CMYA5]] | +0.77 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[YIPF7]] | +0.77 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[CLDN15]] | +0.76 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.75 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.74 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[LINC01618]] | +0.73 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ZNF271P]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GRK7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02889]] | B | LINC02889 activity raises GRK7's level | lines that do not express LINC02889 (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without LINC02889 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, SAMD5, ENSG00000226640; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.8, -15.1); signed map (14.1, 4.6). **Vector** length 82.1, 15.0% of its response variance represented; |z| ≥ 3 in 1,166 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +21.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +14.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.7 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.9 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +7.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.9 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.3 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor kinase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:141,763,408-141,819,352 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GPRK7 |
| Gene groups (HGNC) | G protein-coupled receptor kinase family |
| Reactome | 4 pathways, smallest: Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTQ7](https://www.uniprot.org/uniprotkb/Q8WTQ7) (Opsin kinase GRK7):

> Retina-specific kinase involved in the regulation of phototransduction, playing a key role in terminating light-activated opsin signals in cone photoreceptors. It phosphorylates medium-wave-sensitive opsins (OPN1MW), and it probably acts also on short-wave-sensitive opsin (OPN1SW). In vitro, it also phosphorylates rhodopsin (RHO).

**Summary**, from NCBI Gene [131890](https://www.ncbi.nlm.nih.gov/gene/131890):

> This gene encodes a member of the guanine nucleotide-binding protein (G protein)-coupled receptor kinase subfamily of the Ser/Thr protein kinase family. It is specifically expressed in the retina and the encoded protein has been shown to phosphorylate cone opsins and initiate their deactivation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17031) · Entrez [131890](https://www.ncbi.nlm.nih.gov/gene/131890) · UniProt [Q8WTQ7](https://www.uniprot.org/uniprotkb/Q8WTQ7) · Ensembl [ENSG00000114124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114124)

## Data

Gene col 3526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3526); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3526]; `tensor/DDL_lfc|DDL_z.npy` [3526]; `embed/gene_vectors.npy` [3526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3526 or target_col == 3526). Every well: [[GRK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
