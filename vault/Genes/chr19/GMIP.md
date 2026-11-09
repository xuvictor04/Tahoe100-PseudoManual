---
symbol: "GMIP"
type: "gene"
col: 1592
ensembl_id: "ENSG00000089639"
name: "GEM interacting protein"
location: "19p13.11"
module: 110
arm: "+"
pooled_cpm: 7.77
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# GMIP

*GEM interacting protein* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.52× (z +5.9, q 2e-06, up in 18 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.725× (z -4.4, q 0.007, down in 16 of 37 measured lines) ⚠ toxic; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.748× (z -4.1, q 0.011, down in 8 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPAR2]] (+0.63, fdr 7e-06, ⚠ same locus), [[TEP1]] (+0.55, fdr 2e-05), [[KCTD5]] (+0.55, fdr 1e-05), [[ARHGEF1]] (+0.55, fdr 1e-05); moves opposite to [[C1QTNF3-AMACR]] (-0.57, fdr 2e-05), [[SMCHD1]] (-0.55, fdr 2e-05), [[MACROD2]] (-0.54, fdr 3e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.9 | 2e-06 | 18/45 (SW1417, SK-MEL-2, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +4.1 | 0.013 | 12/44 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.69×** | +3.9 | 0.020 | 3/27 (HEC-1-A, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 1.18× | +3.2 | 0.18 | 9/46 (LS 180, A498, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | 1.26× | +3.1 | 0.22 | 8/35 (KATO III, SW1417, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1592.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.725×** | -4.4 | 0.007 | 16/37 (NCI-H1792, A498, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.748×** | -4.1 | 0.011 | 8/46 (H4, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.823×** | -3.9 | 0.015 | 7/46 (RPMI-7951, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.760×** | -3.9 | 0.015 | 9/47 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -3.8 | 0.017 | 11/46 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.616×** | -3.6 | 0.033 | 12/44 (A-427, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.822×** | -3.2 | 0.093 | 7/48 (NCI-H460, SW 1088, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.791×** | -3.2 | 0.099 | 11/44 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.800×** | -3.2 | 0.099 | 8/47 (HepG2/C3A, hTERT-HPNE, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.802×** | -3.1 | 0.100 | 11/47 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.73 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 5.38 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0778× (z -8.8) |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0356× (z -11.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0679× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 5.68 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0964× (z -9.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SNU-423 (line)]] | alt | 7.01 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.120× (z -9.0) |
| [[A-172 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPAR2]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.5 kb, same strand: neighbours can correlate without regulation) |
| [[TEP1]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[KCTD5]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ARHGEF1]] | +0.55 | +0.55 / +0.64 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[ZNF778]] | +0.54 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[PXN]] | +0.52 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DVL3]] | +0.52 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[ITGA2-AS1]] | +0.51 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[PNP]] | +0.51 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ZNF275]] | +0.51 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ZNF83]] | +0.50 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ZNF558]] | +0.50 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.50 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF3-AMACR]] | -0.57 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[SMCHD1]] | -0.55 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[MACROD2]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ZBTB20]] | -0.50 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[BABAM2]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[WDPCP]] | -0.49 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[SPTLC3]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[TPR]] | -0.47 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[ING3]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TBL1XR1]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MTUS1]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LGR4]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises GMIP's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.1, 33.8); signed map (-2.4, 32.2). **Vector** length 57.9, 7.64% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +2.9 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +2.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | GEM interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,629,476-19,643,657 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGAP46 |
| Gene groups (HGNC) | AH/BAR family Rho GTPase activating proteins |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P107](https://www.uniprot.org/uniprotkb/Q9P107) (GEM-interacting protein):

> Stimulates, in vitro and in vivo, the GTPase activity of RhoA.

**Summary**, from NCBI Gene [51291](https://www.ncbi.nlm.nih.gov/gene/51291):

> This gene encodes a member of the ARHGAP family of Rho/Rac/Cdc42-like GTPase activating proteins. The encoded protein interacts with the Ras-related protein Gem through its N-terminal domain. Separately, it interacts with RhoA through a RhoGAP domain, and stimulates RhoA-dependent GTPase activity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:24852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24852) · Entrez [51291](https://www.ncbi.nlm.nih.gov/gene/51291) · UniProt [Q9P107](https://www.uniprot.org/uniprotkb/Q9P107) · Ensembl [ENSG00000089639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089639)

## Data

Gene col 1592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1592); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1592]; `tensor/DDL_lfc|DDL_z.npy` [1592]; `embed/gene_vectors.npy` [1592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1592 or target_col == 1592). Every well: [[GMIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
