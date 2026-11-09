---
symbol: "CENPB"
type: "gene"
col: 4666
ensembl_id: "ENSG00000125817"
name: "centromere protein B"
location: "20p13"
module: 11
arm: "+"
pooled_cpm: 16.74
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CENPB

*centromere protein B* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.19× (z +6.8, q 7e-09, up in 18 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.74× (z +4.8, q 3e-04, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.662× (z -5.2, q 1e-04, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GALT6]] (+0.70, fdr 7e-06), [[KRI1]] (+0.66, fdr 1e-05), [[RRS1]] (+0.66, fdr 7e-06); moves opposite to [[VDAC1P8]] (-0.65, fdr 1e-05), [[PMS2P4-1]] (-0.58, fdr 3e-05), [[C14orf28]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +6.8 | 7e-09 | 18/30 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +5.2 | 4e-05 | 17/32 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.2 | 4e-05 | 38/43 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.74×** | +4.8 | 3e-04 | 35/47 (NCI-H1792, PANC-1, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.6 | 0.037 | 4/48 (BT-474, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +3.5 | 0.038 | 20/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +3.4 | 0.046 | 19/47 (A549, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.4 | 0.046 | 19/47 (KATO III, SW480, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.44×** | +3.3 | 0.068 | 23/37 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -5.2 | 1e-04 | 28/45 (HEC-1-A, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -4.0 | 0.015 | 26/47 (AN3 CA, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.731×** | -3.9 | 0.015 | 24/47 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.679×** | -3.5 | 0.077 | 23/47 (SNU-1, C32, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.700× | -3.2 | 0.16 | 21/48 (SW480, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.703× | -3.1 | 0.16 | 19/47 (LS 180, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0805× (z -11.6) |
| [[A-172 (line)]] | wt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -10.9) |
| [[J82 (line)]] | alt | 21.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.167× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 9.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.7) |
| [[SNU-1 (line)]] | wt | 25.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -9.5) |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALT6]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[KRI1]] | +0.66 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[RRS1]] | +0.66 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ABCF1]] | +0.62 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[MAGEF1]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[DDX10]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[CCDC57]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[HERPUD2-AS1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BAZ1B]] | +0.59 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[YLPM1]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[INTS5]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[EXOSC2]] | +0.58 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VDAC1P8]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | -0.58 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[C14orf28]] | -0.57 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ATPAF1]] | -0.56 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ACOX1]] | -0.52 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[TSNAX-DISC1]] | -0.52 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[APTR]] | -0.52 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[RARS2]] | -0.52 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[SELENOW]] | -0.52 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[ARPC3]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PIK3C2A]] | -0.51 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[ADCY10]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.362). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.8, -0.6); signed map (9.4, -48.4). **Vector** length 80.6, 18.9% of its response variance represented; |z| ≥ 3 in 646 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +3.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.8 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | +6.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,783,851-3,786,740 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [P07199](https://www.uniprot.org/uniprotkb/P07199) (Major centromere autoantigen B):

> Interacts with centromeric heterochromatin in chromosomes and binds to a specific 17 bp subset of alphoid satellite DNA, called the CENP-B box. May organize arrays of centromere satellite DNA into a higher-order structure which then directs centromere formation and kinetochore assembly in mammalian chromosomes (Probable).

**Summary**, from NCBI Gene [1059](https://www.ncbi.nlm.nih.gov/gene/1059):

> This gene product is a highly conserved protein that facilitates centromere formation. It is a DNA-binding protein that is derived from transposases of the pogo DNA transposon family. It contains a helix-loop-helix DNA binding motif at the N-terminus, and a dimerization domain at the C-terminus. The DNA binding domain recognizes and binds a 17-bp sequence (CENP-B box) in the centromeric alpha satellite DNA. This protein is proposed to play an important role in the assembly of specific …

**Accessions** — [HGNC:1852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1852) · Entrez [1059](https://www.ncbi.nlm.nih.gov/gene/1059) · UniProt [P07199](https://www.uniprot.org/uniprotkb/P07199) · Ensembl [ENSG00000125817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125817)

## Data

Gene col 4666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4666); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4666]; `tensor/DDL_lfc|DDL_z.npy` [4666]; `embed/gene_vectors.npy` [4666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4666 or target_col == 4666). Every well: [[CENPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
