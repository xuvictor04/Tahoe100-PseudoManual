---
symbol: "PANK4"
type: "gene"
col: 8111
ensembl_id: "ENSG00000157881"
name: "pantothenate kinase 4 (inactive)"
location: "1p36.32"
module: 138
arm: "+"
pooled_cpm: 7.15
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# PANK4

*pantothenate kinase 4 (inactive)* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.10× (z +8.3, q 8e-14, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.525× (z -6.9, q 3e-09, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP7]] (+0.59, fdr 1e-05), [[MED16]] (+0.59, fdr 1e-05), [[SETD1A]] (+0.57, fdr 1e-05); moves opposite to [[RSL1D1-DT]] (-0.50, fdr 7e-05), [[ARID4B]] (-0.50, fdr 4e-05), [[HSDL2-AS1]] (-0.50, fdr 4e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.10×** | +8.3 | 8e-14 | 36/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +5.6 | 5e-06 | 23/46 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.5 | 8e-06 | 25/44 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +4.5 | 0.001 | 20/46 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +3.8 | 0.017 | 14/47 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.019 | 11/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.34× | +3.2 | 0.10 | 11/47 (HCT15, NCI-H2030, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -6.9 | 3e-09 | 24/45 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -5.9 | 8e-07 | 25/44 (SW 900, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.653×** | -4.7 | 4e-04 | 19/33 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -3.8 | 0.018 | 20/44 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.39 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0675× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 4.42 | 0 | 2 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM 0.0394× (z -11.6) |
| [[SW 900 (line)]] | alt | 8.05 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -8.8) |
| [[A-427 (line)]] | wt | 8.51 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[C32 (line)]] | wt | 7.40 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0886× (z -9.4) |
| [[HOP62 (line)]] | alt | 8.38 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0422× (z -15.8) |
| [[HT-29 (line)]] | alt | 7.26 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 8.20 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0776× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 4.36 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 6.11 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.324× (z -8.7) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW1417 (line)]] | alt | 3.92 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0771× (z -9.4) |
| [[A-172 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP7]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MED16]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[SETD1A]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[USP19]] | +0.57 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[MIER2]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ANAPC2]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LRCH4]] | +0.56 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[CEP72]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[KMT2B]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.55 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[NCKIPSD]] | +0.55 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[RTEL1]] | +0.54 | +0.59 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSL1D1-DT]] | -0.50 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[ARID4B]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[HSDL2-AS1]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[OOEP]] | -0.50 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[EIF3J-DT]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[YME1L1]] | -0.48 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[KPNB1-DT]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[MSTO1]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MROH8]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SMC5-DT]] | -0.47 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[LINC01019]] | -0.47 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[ADNP-AS1]] | -0.46 | -0.39 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PANK4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[POTEE]] | B | POTEE activity raises PANK4's level | lines that do not express POTEE (29) vs lines expressing it (21) | 1.29× lower at baseline in the lines without POTEE | 0.054 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.4, -24.2); signed map (-11.0, -31.5). **Vector** length 60.0, 8.38% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | +2.2 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.7 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.1 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.6 | +2.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Pentoxifylline (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -2.2 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | pantothenate kinase 4 (inactive) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:2,508,537-2,526,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10782 |
| Gene groups (HGNC) | Pantothenate kinase family |
| Reactome | 3 pathways, smallest: Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVE7](https://www.uniprot.org/uniprotkb/Q9NVE7) (4'-phosphopantetheine phosphatase):

> Phosphatase which shows a preference for 4'-phosphopantetheine and its oxidatively damaged forms (sulfonate or S-sulfonate), providing strong indirect evidence that the phosphatase activity pre-empts damage in the coenzyme A (CoA) pathway. Hydrolyzing excess 4'-phosphopantetheine could constitute a directed overflow mechanism to prevent its oxidation to the S-sulfonate, sulfonate, or other forms. Hydrolyzing 4'-phosphopantetheine sulfonate or S-sulfonate would forestall their conversion to …

**Summary**, from NCBI Gene [55229](https://www.ncbi.nlm.nih.gov/gene/55229):

> This gene encodes a protein belonging to the pantothenate kinase family. Pantothenate kinase is a key regulatory enzyme in the biosynthesis of coenzyme A (CoA) in bacteria and mammalian cells. It catalyzes the first committed step in the universal biosynthetic pathway leading to CoA and is itself subject to regulation through feedback inhibition by CoA. This family member is most abundant in muscle but is expressed in all tissues. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19366) · Entrez [55229](https://www.ncbi.nlm.nih.gov/gene/55229) · UniProt [Q9NVE7](https://www.uniprot.org/uniprotkb/Q9NVE7) · Ensembl [ENSG00000157881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157881)

## Data

Gene col 8111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8111); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8111]; `tensor/DDL_lfc|DDL_z.npy` [8111]; `embed/gene_vectors.npy` [8111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8111 or target_col == 8111). Every well: [[PANK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PANK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
