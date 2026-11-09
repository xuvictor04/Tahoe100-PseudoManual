---
symbol: "HMBS"
type: "gene"
col: 14987
ensembl_id: "ENSG00000256269"
name: "hydroxymethylbilane synthase"
location: "11q23.3"
module: 33
arm: "+"
pooled_cpm: 4.93
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# HMBS

*hydroxymethylbilane synthase* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.76× (z +8.4, q 4e-14, up in 17 of 23 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.93× (z +5.4, q 6e-06, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.589× (z -4.4, q 0.006, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP2]] (+0.68, fdr 7e-06), [[RITA1]] (+0.68, fdr 7e-06), [[POLR3B]] (+0.66, fdr 7e-06); moves opposite to [[OPTN]] (-0.64, fdr 7e-06), [[YPEL5]] (-0.60, fdr 1e-05), [[TXNDC16]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MANEAL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.76×** | +8.4 | 4e-14 | 17/23 (LS 180, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.80×** | +7.1 | 4e-10 | 5/6 (A498, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.25×** | +6.1 | 3e-07 | 6/13 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.01×** | +5.7 | 1e-06 | 26/47 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +5.4 | 6e-06 | 29/46 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.80×** | +4.9 | 1e-04 | 26/46 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.48×** | +4.5 | 5e-04 | 15/39 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.84×** | +4.2 | 0.002 | 11/25 (SW1417, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.65×** | +4.1 | 0.002 | 12/27 (NCI-H23, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.38×** | +3.7 | 0.013 | 12/45 (SW48, SW480, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +3.5 | 0.021 | 14/47 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.53×** | +3.5 | 0.021 | 5/39 (SW480, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.19×** | +3.3 | 0.036 | 5/33 (SW480, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.036 | 10/46 (LOX-IMVI, LS 180, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.62×** | +3.3 | 0.036 | 6/29 (NCI-H2347, A549, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **2.07×** | +3.1 | 0.065 | 3/26 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.05×** | +3.1 | 0.074 | 6/35 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -4.4 | 0.006 | 18/46 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -4.1 | 0.011 | 15/46 (HepG2/C3A, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.044 | 14/38 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.485× | -3.1 | 0.26 | 8/42 (SNU-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.772× | -3.0 | 0.26 | 12/47 (KATO III, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.08 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0613× (z -9.0) |
| [[KATO III (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 7.27 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0775× (z -9.8) |
| [[SW1417 (line)]] | alt | 5.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0826× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP2]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RITA1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[POLR3B]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[WDR18]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[POLR3H]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[EIPR1]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[PGAM5]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[POLR1B]] | +0.62 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NAA15]] | +0.62 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[MRPL4]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NKRF]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SNRPD1]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPTN]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[YPEL5]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[TXNDC16]] | -0.59 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[HLA-A]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CREBRF]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[RGPD2]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANEAL]] | B | MANEAL activity raises HMBS's level | lines that do not express MANEAL (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without MANEAL | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[OAF]] | C | OAF activity lowers HMBS's level | lines that do not express OAF (4) vs lines expressing it (46) | 1.57× higher at baseline in the lines without OAF | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.3, -41.0); signed map (-10.7, -50.9). **Vector** length 57.3, 9.05% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | hydroxymethylbilane synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,084,866-119,093,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PBGD, UPS, PORC |
| Hallmark sets | HEME_METABOLISM, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P08397](https://www.uniprot.org/uniprotkb/P08397) (Porphobilinogen deaminase):

> As part of the heme biosynthetic pathway, catalyzes the sequential polymerization of four molecules of porphobilinogen to form hydroxymethylbilane, also known as preuroporphyrinogen. Catalysis begins with the assembly of the dipyrromethane cofactor by the apoenzyme from two molecules of porphobilinogen or from preuroporphyrinogen. The covalently linked cofactor acts as a primer, around which the tetrapyrrole product is assembled. In the last step of catalysis, the product, preuroporphyrinogen, …

**Summary**, from NCBI Gene [3145](https://www.ncbi.nlm.nih.gov/gene/3145):

> This gene encodes a member of the hydroxymethylbilane synthase superfamily. The encoded protein is the third enzyme of the heme biosynthetic pathway and catalyzes the head to tail condensation of four porphobilinogen molecules into the linear hydroxymethylbilane. Mutations in this gene are associated with the autosomal dominant disease acute intermittent porphyria. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4982) · Entrez [3145](https://www.ncbi.nlm.nih.gov/gene/3145) · UniProt [P08397](https://www.uniprot.org/uniprotkb/P08397) · Ensembl [ENSG00000256269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256269)

## Data

Gene col 14987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14987); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14987]; `tensor/DDL_lfc|DDL_z.npy` [14987]; `embed/gene_vectors.npy` [14987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14987 or target_col == 14987). Every well: [[HMBS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMBS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
