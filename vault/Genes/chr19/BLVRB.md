---
symbol: "BLVRB"
type: "gene"
col: 1607
ensembl_id: "ENSG00000090013"
name: "biliverdin reductase B"
location: "19q13.2"
module: 3
arm: "+"
pooled_cpm: 33.12
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# BLVRB

*biliverdin reductase B* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.31× (z +7.7, q 7e-12, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.171×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (H4 0.159×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF181]] (+0.73, fdr 7e-06), [[MGST3]] (+0.70, fdr 7e-06), [[SLC22A18]] (+0.69, fdr 1e-05); moves opposite to [[SRSF1]] (-0.69, fdr 7e-06), [[XRCC5]] (-0.67, fdr 1e-05), [[SYNCRIP]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CSTB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.31×** | +7.7 | 7e-12 | 41/48 (COLO 205, HEC-1-A, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +6.2 | 1e-07 | 37/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +6.1 | 2e-07 | 30/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +5.6 | 4e-06 | 34/48 (COLO 205, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +5.4 | 9e-06 | 34/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +5.1 | 3e-05 | 37/48 (BT-474, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +5.0 | 4e-05 | 34/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +4.5 | 6e-04 | 34/47 (SW48, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.033 | 27/48 (COLO 205, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.053 | 24/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.26× | +3.0 | 0.13 | 20/48 (SHP-77, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1607.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.171×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (H4 0.159×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.475× | -3.6 | 0.16 | 26/46 (Panc 03.27, AsPC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.767× | -3.4 | 0.16 | 25/47 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | 0.503× | -3.3 | 0.18 | 25/49 (Panc 03.27, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 80.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 28.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.08× (z +8.5) | — |
| [[H4 (line)]] | wt | 63.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H460 (line)]] | wt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.8) | — |
| [[RKO (line)]] | wt | 20.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -13.8) |
| [[A-172 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF181]] | +0.73 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[MGST3]] | +0.70 | +0.60 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[SLC22A18]] | +0.69 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[JOSD2]] | +0.68 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[FTL]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RBIS]] | +0.67 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[CAMLG]] | +0.67 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.66 | +0.55 / +0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.66 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SIRT2]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TOM1]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[CIAO2B]] | +0.64 | +0.41 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.69 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.67 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[SYNCRIP]] | -0.66 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[SSU72]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[MCM7]] | -0.65 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[EIF4G1]] | -0.64 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[PCBD2]] | -0.64 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | -0.63 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.63 | -0.58 / -0.71 | both halves | 7e-06 |  |
| [[DARS2]] | -0.62 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[ADAT1]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[U2AF2]] | -0.62 | -0.48 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSTB]] | B | CSTB activity raises BLVRB's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without CSTB | 0.051 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers BLVRB's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers BLVRB's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRSS8]] | B | PRSS8 activity raises BLVRB's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.23× lower at baseline in the lines without PRSS8 | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.1, -25.7); signed map (-25.7, 9.1). **Vector** length 114, 35.8% of its response variance represented; |z| ≥ 3 in 693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.2 | +7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.1 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +5.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.6 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -5.7 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | biliverdin reductase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,447,765-40,465,764 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR43U1; previously FLR |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; Flavoproteins |
| Hallmark sets | XENOBIOTIC_METABOLISM, HEME_METABOLISM, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 6 pathways, smallest: Heme degradation; Metabolism of porphyrins; Cytoprotection by HMOX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P30043](https://www.uniprot.org/uniprotkb/P30043) (Flavin reductase):

> Enzyme that can both act as a NAD(P)H-dependent reductase and a S-nitroso-CoA-dependent nitrosyltransferase. Promotes fetal heme degradation during development. Also expressed in adult tissues, where it acts as a regulator of hematopoiesis, intermediary metabolism (glutaminolysis, glycolysis, TCA cycle and pentose phosphate pathway) and insulin signaling. Has a broad specificity oxidoreductase activity by catalyzing the NAD(P)H-dependent reduction of a variety of flavins, such as riboflavin, …

**Summary**, from NCBI Gene [645](https://www.ncbi.nlm.nih.gov/gene/645):

> Enables biliverdin reductase [NAD(P)H] activity; peptidyl-cysteine S-nitrosylase activity; and riboflavin reductase (NADPH) activity. Involved in heme catabolic process; megakaryocyte differentiation; and negative regulation of insulin receptor signaling pathway. Located in cytosol. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1063) · Entrez [645](https://www.ncbi.nlm.nih.gov/gene/645) · UniProt [P30043](https://www.uniprot.org/uniprotkb/P30043) · Ensembl [ENSG00000090013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090013)

## Data

Gene col 1607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1607); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1607]; `tensor/DDL_lfc|DDL_z.npy` [1607]; `embed/gene_vectors.npy` [1607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1607 or target_col == 1607). Every well: [[BLVRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLVRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
