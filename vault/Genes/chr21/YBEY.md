---
symbol: "YBEY"
type: "gene"
col: 11279
ensembl_id: "ENSG00000182362"
name: "ybeY metalloendoribonuclease"
location: "21q22.3"
module: 114
arm: "+"
pooled_cpm: 6.76
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# YBEY

*ybeY metalloendoribonuclease* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.19× (z +7.7, q 6e-12, up in 8 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.66× (z +3.5, q 0.039, up in 9 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.647× (z -6.3, q 2e-07, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf56]] (+0.69, fdr 1e-05), [[MRPL32]] (+0.68, fdr 1e-05), [[ZCCHC10]] (+0.66, fdr 1e-05); moves opposite to [[ACTB]] (-0.63, fdr 1e-05), [[PRPF8]] (-0.60, fdr 1e-05), [[ANXA2]] (-0.60, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.7 | 6e-12 | 8/13 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.6 | 9e-12 | 23/28 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +4.8 | 2e-04 | 9/20 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.9 | 0.011 | 9/34 (NCI-H2347, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.6 | 0.039 | 14/43 (A-427, RPMI-7951, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +3.5 | 0.039 | 9/31 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.062 | 5/44 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.57× | +3.1 | 0.11 | 8/44 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.57× | +3.1 | 0.11 | 4/42 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.647×** | -6.3 | 2e-07 | 29/43 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.374×** | -5.2 | 3e-05 | 24/46 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.376×** | -5.2 | 3e-05 | 24/43 (SW480, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.657×** | -4.3 | 0.003 | 14/46 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.675×** | -4.0 | 0.007 | 16/47 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.703×** | -3.4 | 0.069 | 16/45 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.725× | -3.0 | 0.21 | 6/47 (C-33 A, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.55 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0838× (z -8.5) |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 11 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf56]] | +0.69 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[MRPL32]] | +0.68 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[ZCCHC10]] | +0.66 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[COA6]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.64 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[EIF1B]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ERVK3-1]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MRPS36]] ⚠ | +0.63 | +0.43 / +0.73 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C11orf1]] | +0.63 | +0.37 / +0.73 | both halves | 9e-05 |  |
| [[FDX2]] | +0.63 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[MAP2K7]] | +0.63 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[SNHG9]] | +0.63 | +0.40 / +0.75 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTB]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[PRPF8]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[ANXA2]] | -0.60 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ILF2]] | -0.58 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[YWHAQ]] | -0.57 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[FLNA]] | -0.57 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[TMED7]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[UGGT1]] | -0.56 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[TXNDC5]] | -0.56 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[AP2M1]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[MYH9]] | -0.56 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.8, -14.7); signed map (-3.0, -7.2). **Vector** length 40.9, 4.68% of its response variance represented; |z| ≥ 3 in 633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +2.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.2 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -3.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.8 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ybeY metalloendoribonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:46,286,342-46,297,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C21orf57 |
| Matched by | ensembl_id |

**Function**, from UniProt [P58557](https://www.uniprot.org/uniprotkb/P58557) (Endoribonuclease YbeY):

> Single strand-specific metallo-endoribonuclease involved in rRNA maturation.

**Summary**, from NCBI Gene [54059](https://www.ncbi.nlm.nih.gov/gene/54059):

> This gene encodes a highly conserved metalloprotein. A similar protein in bacteria acts as an endoribonuclease, and is thought to function in ribosomal RNA maturation and ribosome assembly. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:1299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1299) · Entrez [54059](https://www.ncbi.nlm.nih.gov/gene/54059) · UniProt [P58557](https://www.uniprot.org/uniprotkb/P58557) · Ensembl [ENSG00000182362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182362)

## Data

Gene col 11279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11279); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11279]; `tensor/DDL_lfc|DDL_z.npy` [11279]; `embed/gene_vectors.npy` [11279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11279 or target_col == 11279). Every well: [[YBEY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YBEY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
