---
symbol: "LYSMD1"
type: "gene"
col: 8644
ensembl_id: "ENSG00000163155"
name: "LysM domain containing 1"
location: "1q21.3"
module: 107
arm: "+"
pooled_cpm: 5.23
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# LYSMD1

*LysM domain containing 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.81× (z +7.6, q 1e-11, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.545× (z -11.1, q 8e-26, down in 29 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMPR2]] (+0.60, fdr 1e-05), [[METTL22]] (+0.60, fdr 1e-05), [[ERCC3]] (+0.59, fdr 7e-06); moves opposite to [[CYFIP1]] (-0.50, fdr 9e-05), [[PFN1]] (-0.49, fdr 4e-04), [[KLF12]] (-0.49, fdr 4e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +7.6 | 1e-11 | 23/45 (NCI-H23, RPMI-7951, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +7.1 | 4e-10 | 13/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +5.6 | 4e-06 | 11/46 (LS 180, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.30× | +3.2 | 0.20 | 3/44 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.20 | 4/36 (SHP-77, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 1.29× | +3.0 | 0.20 | 4/36 (A-427, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.20 | 4/46 (HEC-1-A, RKO, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8644.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -11.1 | 8e-26 | 29/39 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.570×** | -7.0 | 8e-10 | 21/44 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.694×** | -4.7 | 4e-04 | 9/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.698×** | -4.7 | 5e-04 | 11/45 (H4, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -4.2 | 0.002 | 15/40 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.711×** | -4.2 | 0.002 | 13/35 (A-427, KATO III, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.738×** | -3.9 | 0.007 | 14/46 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -3.2 | 0.10 | 13/45 (NCI-H460, A-172, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.789× | -3.1 | 0.12 | 9/45 (A-427, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.790× | -3.1 | 0.12 | 6/45 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.636× | -3.1 | 0.12 | 10/39 (NCI-H1573, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.58 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.7) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.3) |
| [[HCT15 (line)]] | alt | 8.64 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0701× (z -9.9) |
| [[Hs 766T (line)]] | wt | 5.30 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -8.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 4.41 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0421× (z -11.8) |
| [[J82 (line)]] | alt | 4.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 4.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 6.86 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0981× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 4.07 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMPR2]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[METTL22]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ERCC3]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TMEM94]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[OGFOD2]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ZNF224]] | +0.58 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[POLL]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[COASY]] | +0.57 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[NAGPA]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZNF266]] | +0.57 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[BABAM1]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[VIPAS39]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYFIP1]] | -0.50 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[PFN1]] | -0.49 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[KLF12]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CALM2]] | -0.47 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LYSMD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAFIP]] | B | MAFIP activity raises LYSMD1's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without MAFIP | 0.088 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.1, -14.9); signed map (-28.8, -19.7). **Vector** length 49.7, 5.69% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.5 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.5 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -3.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LysM domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,159,748-151,165,948 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SB145, MGC35223, RP11-68I18.5 |
| Gene groups (HGNC) | LysM domain containing |
| Matched by | ensembl_id |

UniProt [Q96S90](https://www.uniprot.org/uniprotkb/Q96S90) carries no function annotation.

**Summary**, from NCBI Gene [388695](https://www.ncbi.nlm.nih.gov/gene/388695):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32070) · Entrez [388695](https://www.ncbi.nlm.nih.gov/gene/388695) · UniProt [Q96S90](https://www.uniprot.org/uniprotkb/Q96S90) · Ensembl [ENSG00000163155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163155)

## Data

Gene col 8644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8644); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8644]; `tensor/DDL_lfc|DDL_z.npy` [8644]; `embed/gene_vectors.npy` [8644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8644 or target_col == 8644). Every well: [[LYSMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYSMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
