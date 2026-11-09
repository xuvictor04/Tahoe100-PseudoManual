---
symbol: "OIT3"
type: "gene"
col: 6152
ensembl_id: "ENSG00000138315"
name: "oncoprotein induced transcript 3"
location: "10q22.1"
module: 39
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# OIT3

*oncoprotein induced transcript 3* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.50× (z +9.3, q 5e-18, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 2.56× (z +7.3, q 5e-11, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.453× (z -6.2, q 3e-07, down in 21 of 43 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.285× (z -5.1, q 9e-05, down in 17 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.87, fdr 7e-06), [[CDKL4]] (+0.84, fdr 7e-06), [[SLC22A14]] (+0.84, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LMO7DN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +9.3 | 5e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.13×** | +7.8 | 2e-12 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **2.56×** | +7.3 | 5e-11 | 27/43 (A498, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +6.5 | 9e-09 | 12/32 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +6.5 | 9e-09 | 6/9 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.4 | 1e-08 | 11/30 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +5.2 | 2e-05 | 12/34 (HOP62, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.97×** | +5.0 | 5e-05 | 13/35 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.49×** | +4.3 | 9e-04 | 9/43 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.73×** | +4.0 | 0.003 | 5/37 (A549, A-427, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +3.7 | 0.013 | 8/44 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.015 | 7/42 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.019 | 4/25 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.094 | 2/43 (NCI-H1573, HEC-1-A) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6152.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.453×** | -6.2 | 3e-07 | 21/43 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.285×** | -5.1 | 9e-05 | 17/35 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.539×** | -4.6 | 9e-04 | 14/41 (NCI-H1573, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Bexarotene (drug)]] 5 µM |  | **0.615×** | -3.8 | 0.020 | 13/43 (A-172, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.614×** | -3.6 | 0.035 | 16/37 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Glasdegib (drug)]] 5 µM | ⚠ unreliable plate only | **0.634×** | -3.6 | 0.035 | 12/43 (SNU-1, COLO 205, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.654×** | -3.3 | 0.072 | 10/28 (LoVo, Hs 766T, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM |  | 0.758× | -3.1 | 0.15 | 5/43 (Hs 766T, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 4.82 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0427× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 9.65 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0430× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 5.80 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0457× (z -10.5) |
| [[KATO III (line)]] | alt | 9.20 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0766× (z -9.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 1.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +8.6) | — |
| [[A-172 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.950 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.87 | +0.86 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CDKL4]] | +0.84 | +0.84 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SLC22A14]] | +0.84 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[MPP4]] | +0.83 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[USP50]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.81 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.81 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HCLS1]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[SLC5A11]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO7DN]] | B | LMO7DN activity raises OIT3's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.23× lower at baseline in the lines without LMO7DN | 0.044 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[MROH3P]] | B | MROH3P activity raises OIT3's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.29× lower at baseline in the lines without MROH3P | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[SMCO2]] | B | SMCO2 activity raises OIT3's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without SMCO2 | 0.067 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[LSMEM2]] | B | LSMEM2 activity raises OIT3's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without LSMEM2 | 0.068 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.883). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.7, -14.3); signed map (17.5, 9.5). **Vector** length 63.7, 9.28% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | oncoprotein induced transcript 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,893,584-72,933,036 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LZP, FLJ39116 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWZ8](https://www.uniprot.org/uniprotkb/Q8WWZ8) (Oncoprotein-induced transcript 3 protein):

> May be involved in hepatocellular function and development.

**Summary**, from NCBI Gene [170392](https://www.ncbi.nlm.nih.gov/gene/170392):

> This gene was identified due to its downregulation in hepatocarcinomas. The encoded protein may be involved in liver development and function. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:29953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29953) · Entrez [170392](https://www.ncbi.nlm.nih.gov/gene/170392) · UniProt [Q8WWZ8](https://www.uniprot.org/uniprotkb/Q8WWZ8) · Ensembl [ENSG00000138315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138315)

## Data

Gene col 6152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6152); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6152]; `tensor/DDL_lfc|DDL_z.npy` [6152]; `embed/gene_vectors.npy` [6152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6152 or target_col == 6152). Every well: [[OIT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OIT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
