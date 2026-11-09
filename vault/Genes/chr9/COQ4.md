---
symbol: "COQ4"
type: "gene"
col: 9420
ensembl_id: "ENSG00000167113"
name: "coenzyme Q4"
location: "9q34.11"
module: 30
arm: "+"
pooled_cpm: 12.21
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# COQ4

*coenzyme Q4* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.70× (z +7.7, q 6e-12, up in 23 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.22× (z +4.2, q 0.006, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.732× (z -6.5, q 5e-08, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC10]] (+0.67, fdr 7e-06), [[FIS1]] (+0.62, fdr 2e-05), [[ATPAF2]] (+0.62, fdr 1e-05); moves opposite to [[CALM2]] (-0.57, fdr 2e-05), [[ANXA5]] (-0.54, fdr 4e-05), [[HNRNPA2B1]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.7 | 6e-12 | 23/34 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.4 | 3e-08 | 23/40 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.006 | 15/48 (RKO, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +4.0 | 0.008 | 15/41 (A-172, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.33×** | +4.0 | 0.008 | 13/46 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.20× | +3.7 | 0.019 | 13/44 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.30×** | +3.7 | 0.019 | 14/24 (HEC-1-A, BT-474, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.020 | 15/44 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.023 | 9/47 (SW480, A-427, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.031 | 11/48 (J82, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.27×** | +3.4 | 0.031 | 7/47 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.25×** | +3.2 | 0.059 | 6/47 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.084 | 5/48 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.084 | 12/42 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.27×** | +3.1 | 0.084 | 11/30 (Hs 766T, SW480, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.732×** | -6.5 | 5e-08 | 32/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.742×** | -6.2 | 2e-07 | 23/45 (Panc 03.27, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.677×** | -5.7 | 2e-06 | 25/47 (HCT15, SNU-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.651× | -3.3 | 0.14 | 10/48 (Hs 766T, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.776× | -3.2 | 0.14 | 4/47 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.6) |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 9.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -8.9) |
| [[SW48 (line)]] | wt | 10.4 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0735× (z -8.5) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC10]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[FIS1]] | +0.62 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[ATPAF2]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NUDT2]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PPOX]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[CBY1]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ACOT8]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ZDHHC24]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZFPL1]] | +0.57 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[FAM174A]] | +0.57 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[MORN4]] | +0.57 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[TENT2]] | +0.57 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM2]] | -0.57 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[ANXA5]] | -0.54 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.54 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[ACSL4]] | -0.53 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[YWHAZ]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.51 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[TPM4]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[MYH9]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CCDC144CP]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[FAT1]] | -0.49 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[EPB41L2]] | -0.49 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[PHEX]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.478). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-32.8, -12.3); signed map (-23.9, -1.0). **Vector** length 55.7, 8.26% of its response variance represented; |z| ≥ 3 in 609 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.6 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.5 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.8 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,322,544-128,334,072 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-92 |
| Gene groups (HGNC) | Decarboxylases |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3A0](https://www.uniprot.org/uniprotkb/Q9Y3A0) (Ubiquinone biosynthesis protein COQ4 homolog, mitochondrial):

> Lyase that catalyzes the C1-decarboxylation of 4-hydroxy-3-methoxy-5-(all-trans-decaprenyl)benzoic acid into 2-methoxy-6-(all-trans-decaprenyl)phenol during ubiquinone biosynthesis.

**Summary**, from NCBI Gene [51117](https://www.ncbi.nlm.nih.gov/gene/51117):

> This gene encodes a component of the coenzyme Q biosynthesis pathway. Coenzyme Q, an essential component of the electron transport chain, shuttles electrons between complexes I or II to complex III of the mitochondrial transport chain. This protein appears to play a structural role in stabilizing a complex that contains most of the coenzyme Q biosynthesis enzymes. Mutations in this gene are associated with mitochondrial disorders linked to coenzyme Q deficiency. Alternative splicing results in …

**Accessions** — [HGNC:19693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19693) · Entrez [51117](https://www.ncbi.nlm.nih.gov/gene/51117) · UniProt [Q9Y3A0](https://www.uniprot.org/uniprotkb/Q9Y3A0) · Ensembl [ENSG00000167113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167113)

## Data

Gene col 9420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9420); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9420]; `tensor/DDL_lfc|DDL_z.npy` [9420]; `embed/gene_vectors.npy` [9420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9420 or target_col == 9420). Every well: [[COQ4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
