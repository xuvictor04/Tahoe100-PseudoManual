---
symbol: "FLRT1"
type: "gene"
col: 4741
ensembl_id: "ENSG00000126500"
name: "fibronectin leucine rich transmembrane protein 1"
location: "11q13.1"
module: 53
arm: "+"
pooled_cpm: 2.21
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# FLRT1

*fibronectin leucine rich transmembrane protein 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.89× (z +16.0, q 0e+00, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.580× (z -5.6, q 1e-05, down in 13 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (A498 0.0711×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[L3MBTL2-AS1]] (+0.73, fdr 7e-06), [[MASP2]] (+0.67, fdr 1e-05), [[DNAH10]] (+0.66, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC7A11-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +16.0 | 0e+00 | 25/31 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +13.8 | 1e-40 | 15/31 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.77×** | +10.9 | 2e-25 | 27/37 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +10.0 | 2e-21 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +9.4 | 5e-19 | 4/10 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.5 | 7e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.0 | 0.006 | 2/11 (A-427, SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.7 | 0.014 | 1/3 (A498) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.7 | 0.015 | 4/17 (HEC-1-A, BT-474, …) | inconsistent across doses | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.37×** | +3.3 | 0.046 | 2/31 (HEC-1-A, SW 900) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.80×** | +3.3 | 0.055 | 0/25 | top dose only | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.069 | 2/27 (NCI-H460, KATO III) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.1 | 0.076 | 0/5 | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.091 | 2/31 (KATO III, C-33 A) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.0 | 0.095 | 4/38 (NCI-H23, C-33 A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4741.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (A498 0.0711×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.580×** | -5.6 | 1e-05 | 13/39 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.618×** | -5.1 | 7e-05 | 10/45 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Trifluridine (drug)]] 0.5 µM |  | 0.727× | -3.2 | 0.25 | 6/38 (SHP-77, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.34 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0711× (z -8.6) |
| [[HS-578T (line)]] | alt | 2.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +11.0) | — |
| [[LoVo (line)]] | wt | 1.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 1.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +9.8) | — |
| [[SW480 (line)]] | alt | 2.11 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.11× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L3MBTL2-AS1]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[MASP2]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[DNAH10]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[LINC00616]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[AZU1]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PEBP4]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CPT1C]] | +0.64 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[SLC8A2]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[EPHA1-AS1]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[RYR1]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MYL6B-AS1]] | +0.63 | +0.47 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A11-AS1]] | B | SLC7A11-AS1 activity lowers FLRT1's level | lines that do not express SLC7A11-AS1 (11) vs lines expressing it (39) | 1.30× higher at baseline in the lines without SLC7A11-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, -16.7); signed map (22.2, 11.8). **Vector** length 42.6, 4.49% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +16.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.0 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.7 | -0.2 |
|  | [[Malotilate (drug)]] 5 µM |  | -0.7 | -1.5 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin leucine rich transmembrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,035,931-64,119,173 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21624, SPG68 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Reactome | 4 pathways, smallest: Downstream signaling of activated FGFR1; Signaling by FGFR1; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZU1](https://www.uniprot.org/uniprotkb/Q9NZU1) (Leucine-rich repeat transmembrane protein FLRT1):

> Plays a role in fibroblast growth factor-mediated signaling cascades that lead to the activation of MAP kinases. Promotes neurite outgrowth via FGFR1-mediated activation of downstream MAP kinases. Promotes an increase both in neurite number and in neurite length. May play a role in cell-cell adhesion and cell guidance via its interaction with ADGRL1/LPHN1 and ADGRL3.

**Summary**, from NCBI Gene [23769](https://www.ncbi.nlm.nih.gov/gene/23769):

> This gene encodes a member of the fibronectin leucine rich transmembrane protein (FLRT) family. The family members may function in cell adhesion and/or receptor signalling. Their protein structures resemble small leucine-rich proteoglycans found in the extracellular matrix. The encoded protein shares sequence similarity with two other family members, FLRT2 and FLRT3. This gene is expressed in kidney and brain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3760) · Entrez [23769](https://www.ncbi.nlm.nih.gov/gene/23769) · UniProt [Q9NZU1](https://www.uniprot.org/uniprotkb/Q9NZU1) · Ensembl [ENSG00000126500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126500)

## Data

Gene col 4741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4741); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4741]; `tensor/DDL_lfc|DDL_z.npy` [4741]; `embed/gene_vectors.npy` [4741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4741 or target_col == 4741). Every well: [[FLRT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLRT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
