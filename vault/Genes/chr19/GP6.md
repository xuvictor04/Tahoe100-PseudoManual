---
symbol: "GP6"
type: "gene"
col: 1520
ensembl_id: "ENSG00000088053"
name: "glycoprotein VI platelet"
location: "19q13.42"
module: 53
arm: "+"
pooled_cpm: 8.49
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# GP6

*glycoprotein VI platelet* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.04× (z +9.1, q 7e-17, up in 32 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H1792 0.106×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0892×; ⚠ toxic; cell-cycle shift, explains ~30% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHKG1]] (+0.73, fdr 7e-06), [[PHYHD1]] (+0.68, fdr 7e-06), [[LSMEM2]] (+0.67, fdr 7e-06); moves opposite to [[ZNF649]] (-0.54, fdr 3e-04), [[TADA2A]] (-0.54, fdr 2e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM83E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +9.1 | 7e-17 | 32/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.3 | 3e-14 | 28/43 (A549, A498, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.5 | 1e-08 | 20/32 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +6.2 | 1e-07 | 22/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +5.7 | 1e-06 | 22/44 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +5.6 | 2e-06 | 23/47 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.4 | 5e-06 | 10/18 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.007 | 13/47 (SW480, A549, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.007 | 11/43 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 14/45 (SNU-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +3.4 | 0.030 | 8/28 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.035 | 6/47 (HT-29, KATO III, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.040 | 5/45 (HS-578T, SW480, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.088 | 5/48 (SHP-77, LoVo, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1520.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H1792 0.106×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0892×; ⚠ toxic; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | 0.571× | -3.7 | 0.12 | 14/40 (SHP-77, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.3 | 0.27 | 9/48 (SNU-1, HCT15, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.837× | -3.2 | 0.28 | 14/46 (NCI-H460, A549, …) | top dose only | position effect removed |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.844× | -3.0 | 0.35 | 3/48 (LOX-IMVI, C-33 A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0892× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 9.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 7.15 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.106× (z -8.9) |
| [[A-172 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKG1]] | +0.73 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[PHYHD1]] | +0.68 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[LSMEM2]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TINCR]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.67 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.66 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MASP2]] | +0.65 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[TTLL13]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PDE2A]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF649]] | -0.54 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[TADA2A]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | FAM83E activity raises GP6's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without FAM83E | 0.091 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[MAP1LC3A]] | C | MAP1LC3A activity lowers GP6's level | lines that do not express MAP1LC3A (4) vs lines expressing it (46) | 1.57× higher at baseline in the lines without MAP1LC3A | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285155; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, -18.2); signed map (13.8, 14.1). **Vector** length 58.3, 8.47% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[NG25 (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | glycoprotein VI platelet |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,013,705-55,038,264 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPVI |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Ig-like cell adhesion molecule family |
| Reactome | 5 pathways, smallest: Platelet Adhesion to exposed collagen; GPVI-mediated activation cascade; Cell surface interactions at the vascular wall |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCN6](https://www.uniprot.org/uniprotkb/Q9HCN6) (Platelet glycoprotein VI):

> Collagen receptor involved in collagen-induced platelet adhesion and activation. Plays a key role in platelet procoagulant activity and subsequent thrombin and fibrin formation. This procoagulant function may contribute to arterial and venous thrombus formation. The signaling pathway involves the FcR gamma-chain, the Src kinases (likely FYN or LYN) and SYK, the adapter protein LAT and leads to the activation of PLCG2.

**Summary**, from NCBI Gene [51206](https://www.ncbi.nlm.nih.gov/gene/51206):

> This gene encodes a platelet membrane glycoprotein of the immunoglobulin superfamily. The encoded protein is a receptor for collagen and plays a critical role in collagen-induced platelet aggregation and thrombus formation. The encoded protein forms a complex with the Fc receptor gamma-chain that initiates the platelet activation signaling cascade upon collagen binding. Mutations in this gene are a cause of platelet-type bleeding disorder-11 (BDPLT11). Alternatively spliced transcript variants …

**Accessions** — [HGNC:14388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14388) · Entrez [51206](https://www.ncbi.nlm.nih.gov/gene/51206) · UniProt [Q9HCN6](https://www.uniprot.org/uniprotkb/Q9HCN6) · Ensembl [ENSG00000088053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088053)

## Data

Gene col 1520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1520); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1520]; `tensor/DDL_lfc|DDL_z.npy` [1520]; `embed/gene_vectors.npy` [1520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1520 or target_col == 1520). Every well: [[GP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
