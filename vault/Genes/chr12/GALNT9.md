---
symbol: "GALNT9"
type: "gene"
col: 11336
ensembl_id: "ENSG00000182870"
name: "polypeptide N-acetylgalactosaminyltransferase 9"
location: "12q24.33"
module: 75
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 32
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# GALNT9

*polypeptide N-acetylgalactosaminyltransferase 9* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.45× (z +14.1, q 4e-42, up in 6 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Proglumide (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0896×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLB1]] (+0.61, fdr 3e-05), [[KCND3]] (+0.57, fdr 3e-05), [[NTRK3]] (+0.56, fdr 9e-05); moves opposite to [[TCTN3]] (-0.47, fdr 4e-05), [[DZANK1]] (-0.46, fdr 5e-04), [[FAM76B]] (-0.45, fdr 9e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IL1R2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NKAIN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +14.1 | 4e-42 | 6/15 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.41×** | +13.6 | 2e-39 | 18/21 (HEC-1-A, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.06×** | +12.7 | 1e-34 | 12/20 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.84×** | +12.7 | 1e-34 | 5/7 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.76×** | +12.1 | 2e-31 | 3/3 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +10.0 | 2e-21 | 3/4 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.19×** | +8.9 | 4e-17 | 14/27 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +7.6 | 1e-12 | 11/18 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.49×** | +7.3 | 2e-11 | 14/27 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +6.8 | 6e-10 | 7/11 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.12×** | +6.0 | 8e-08 | 12/27 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.00×** | +5.6 | 1e-06 | 10/25 (A498, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +5.5 | 2e-06 | 3/12 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +5.5 | 2e-06 | 12/22 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.04×** | +4.7 | 1e-04 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +4.3 | 6e-04 | 10/21 (A498, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +3.9 | 0.003 | 10/19 (SHP-77, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.004 | 1/28 (A498) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.009 | 4/21 (A498, H4, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +3.5 | 0.010 | 8/24 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.55×** | +3.5 | 0.010 | 0/13 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11336.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Proglumide (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0896×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.638× | -3.6 | 0.15 | 8/28 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.89 | 2 | 1 | [[Auranofin (drug)]] 5 µM 14.8× (z +9.8) | [[Proglumide (drug)]] 0.05 µM 0.0896× (z -8.9) |
| [[A498 (line)]] | wt | 11.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 5.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +10.1) | — |
| [[A-172 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.639 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.749 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.836 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.786 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.601 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLB1]] | +0.61 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[KCND3]] | +0.57 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[NTRK3]] | +0.56 | +0.37 / +0.62 | both halves | 9e-05 |  |
| [[LINC01933]] | +0.56 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[LINC00592]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CACNA1E]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CBFA2T3]] | +0.53 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[ZNF365]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[LINC01033]] | +0.52 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[SLC35F1]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[CD22]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ANO1]] | +0.51 | +0.36 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTN3]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DZANK1]] | -0.46 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[FAM76B]] | -0.45 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[PGRMC2]] | -0.45 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[POLE3]] | -0.44 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[KLHDC10]] | -0.44 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[COX14]] | -0.43 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[CA5BP1]] | -0.43 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[CASP8AP2]] | -0.43 | -0.27 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1R2]] | B | IL1R2 activity raises GALNT9's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 1.81× lower at baseline in the lines without IL1R2 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[LAD1]] | B | LAD1 activity raises GALNT9's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 1.48× lower at baseline in the lines without LAD1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NKAIN1]] | B | GALNT9 activity lowers NKAIN1's level | lines that do not express GALNT9 (18) vs lines expressing it (32) | 1.67× higher at baseline in the lines without GALNT9 | 0.091 | ⚠ within organs, on part of the lines; also absent: CDA, LINC01605, TMEM92; maybe low, not absent |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.6, 37.4); signed map (33.9, 22.3). **Vector** length 41.3, 6.89% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | +0.0 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.1 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,196,372-132,329,589 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GALNAC-T9 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCQ5](https://www.uniprot.org/uniprotkb/Q9HCQ5) (Polypeptide N-acetylgalactosaminyltransferase 9):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Does not glycosylate apomucin or SDC3.

**Summary**, from NCBI Gene [50614](https://www.ncbi.nlm.nih.gov/gene/50614):

> This gene encodes a member of the UDP-N-acetyl-alpha-D-galactosamine:polypeptide N-acetylgalactosaminyltransferase (GalNAc-T) family of enzymes. GalNAc-Ts initiate mucin-type O-linked glycosylation in the Golgi apparatus by catalyzing the transfer of GalNAc to serine and threonine residues on target proteins. They are characterized by an N-terminal transmembrane domain, a stem region, a lumenal catalytic domain containing a GT1 motif and Gal/GalNAc transferase motif, and a C-terminal …

**Accessions** — [HGNC:4131](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4131) · Entrez [50614](https://www.ncbi.nlm.nih.gov/gene/50614) · UniProt [Q9HCQ5](https://www.uniprot.org/uniprotkb/Q9HCQ5) · Ensembl [ENSG00000182870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182870)

## Data

Gene col 11336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11336); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11336]; `tensor/DDL_lfc|DDL_z.npy` [11336]; `embed/gene_vectors.npy` [11336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11336 or target_col == 11336). Every well: [[GALNT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
