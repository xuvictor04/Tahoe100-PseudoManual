---
symbol: "CISD1"
type: "gene"
col: 4382
ensembl_id: "ENSG00000122873"
name: "CDGSH iron sulfur domain 1"
location: "10q21.1"
module: 190
arm: "+"
pooled_cpm: 27.7
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# CISD1

*CDGSH iron sulfur domain 1* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +8.9, q 2e-16, up in 38 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +8.0, q 2e-13, up in 35 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.400×, HS-578T 0.338×); [[Fluvoxamine (drug)]] 5 µM in 1 line (AN3 CA 0.0736×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLVRA]] (+0.57, fdr 1e-05), [[KLHL8]] (+0.57, fdr 2e-05), [[ATOX1]] (+0.55, fdr 2e-05); moves opposite to [[BTBD19]] (-0.52, fdr 4e-05), [[PPP1R10]] (-0.51, fdr 5e-05), [[NRAS]] (-0.51, fdr 3e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PKIG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.25×** | +8.9 | 2e-16 | 38/44 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.0 | 2e-13 | 35/47 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.13×** | +8.0 | 2e-13 | 22/34 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.07×** | +8.0 | 2e-13 | 40/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.95×** | +7.4 | 2e-11 | 38/48 (NCI-H460, NCI-H2347, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +6.9 | 5e-10 | 39/48 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.84×** | +6.7 | 2e-09 | 33/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +5.9 | 2e-07 | 36/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +5.8 | 3e-07 | 30/47 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.65×** | +5.1 | 2e-05 | 27/38 (J82, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +5.1 | 2e-05 | 29/47 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.54×** | +4.6 | 2e-04 | 25/46 (SW1417, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 28/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.016 | 23/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.39×** | +3.5 | 0.016 | 21/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.024 | 17/48 (A-427, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4382.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.400×, HS-578T 0.338×); [[Fluvoxamine (drug)]] 5 µM in 1 line (AN3 CA 0.0736×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.516× | -3.5 | 0.10 | 22/46 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.799× | -3.5 | 0.10 | 23/47 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | 0.518× | -3.5 | 0.10 | 20/48 (SNU-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0736× (z -9.0) |
| [[HOP62 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.0) |
| [[RKO (line)]] | wt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.3) |
| [[A-172 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLVRA]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[KLHL8]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[ATOX1]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[INTS10]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[ECI2]] | +0.52 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[CMTM8]] | +0.52 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[RBIS]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SHPRH]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[CIBAR1]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[UBA3]] | +0.50 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[DUXAP10]] | +0.50 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[TMEM161A]] | +0.50 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD19]] | -0.52 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[PPP1R10]] | -0.51 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[NRAS]] | -0.51 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[FSCN2]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[HPX]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ZDHHC11]] | -0.50 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[SCAF1]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[LINC00174]] | -0.49 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[SRSF3]] | -0.48 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[PLEC]] | -0.48 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ADAMTSL4-AS2]] | -0.48 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[SRSF6]] | -0.47 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIG]] | B | PKIG activity raises CISD1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without PKIG | 0.063 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.7, -12.0); signed map (-38.8, -19.3). **Vector** length 71.0, 16.0% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +6.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -2.2 | +5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | CDGSH iron sulfur domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:58,269,162-58,289,586 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS029, mitoNEET; previously C10orf70, ZCD1 |
| Gene groups (HGNC) | CDGSH iron sulfur domain containing; Transaminases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ45](https://www.uniprot.org/uniprotkb/Q9NZ45) (CDGSH iron-sulfur domain-containing protein 1):

> L-cysteine transaminase that catalyzes the reversible transfer of the amino group from L-cysteine to the alpha-keto acid 2-oxoglutarate to respectively form 2-oxo-3-sulfanylpropanoate and L-glutamate. The catalytic cycle occurs in the presence of pyridoxal 5'-phosphate (PLP) cofactor that facilitates transamination by initially forming an internal aldimine with the epsilon-amino group of active site Lys-55 residue on the enzyme (PLP-enzyme aldimine), subsequently displaced by formation of an …

**Summary**, from NCBI Gene [55847](https://www.ncbi.nlm.nih.gov/gene/55847):

> This gene encodes a protein with a CDGSH iron-sulfur domain and has been shown to bind a redox-active [2Fe-2S] cluster. The encoded protein has been localized to the outer membrane of mitochondria and is thought to play a role in regulation of oxidation. Genes encoding similar proteins are located on chromosomes 4 and 17, and a pseudogene of this gene is located on chromosome 2. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:30880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30880) · Entrez [55847](https://www.ncbi.nlm.nih.gov/gene/55847) · UniProt [Q9NZ45](https://www.uniprot.org/uniprotkb/Q9NZ45) · Ensembl [ENSG00000122873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122873)

## Data

Gene col 4382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4382); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4382]; `tensor/DDL_lfc|DDL_z.npy` [4382]; `embed/gene_vectors.npy` [4382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4382 or target_col == 4382). Every well: [[CISD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CISD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
