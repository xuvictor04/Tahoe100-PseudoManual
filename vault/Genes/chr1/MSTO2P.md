---
symbol: "MSTO2P"
type: "gene"
col: 12786
ensembl_id: "ENSG00000203761"
name: "misato family member 2, pseudogene"
location: "1q22"
module: 42
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MSTO2P

*misato family member 2, pseudogene* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.29× (z +6.4, q 7e-08, up in 18 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.02× (z +5.1, q 8e-05, up in 15 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.314× (z -8.2, q 1e-13, down in 24 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO2]] (+0.76, fdr 7e-06), [[SEPTIN7P14]] (+0.74, fdr 7e-06), [[DPH7]] (+0.72, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.68, fdr 1e-05), [[LINC02307]] (-0.63, fdr 1e-05), [[MED13]] (-0.62, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.29×** | +6.4 | 7e-08 | 18/46 (A-172, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +5.1 | 8e-05 | 15/44 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +5.0 | 1e-04 | 10/40 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.16×** | +4.4 | 0.002 | 6/23 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +4.1 | 0.006 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.56×** | +3.6 | 0.031 | 0/5 | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.314×** | -8.2 | 1e-13 | 24/36 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.529×** | -4.7 | 8e-04 | 16/42 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -4.1 | 0.007 | 11/33 (LoVo, SHP-77, …) | two highest doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.694×** | -3.5 | 0.075 | 17/27 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.714× | -3.3 | 0.13 | 10/44 (HT-29, A-172, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.654× | -3.1 | 0.16 | 15/44 (A549, CFPAC-1, …) | two highest doses | composition shift; position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | 0.663× | -3.0 | 0.17 | 12/44 (A-172, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.653× | -3.0 | 0.17 | 8/27 (CFPAC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.65 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0228× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 2.60 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0689× (z -9.2) ⚠ cell-cycle shift, explains ~95% of this change |
| [[HS-578T (line)]] | alt | 3.30 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0325× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 2.63 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.05 µM 0.0352× (z -9.0) |
| [[A-172 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.949 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.541 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.664 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO2]] | +0.76 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[SEPTIN7P14]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[DPH7]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.72 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[DDB1]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.71 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[ABHD17A]] | +0.71 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[RNF216P1]] | +0.69 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[STT3A]] | +0.68 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[NUS1]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[UTP6]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[COPG1]] | +0.68 | +0.77 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.68 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.63 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[MED13]] | -0.62 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TSC22D1]] | -0.61 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[WAC-AS1]] | -0.59 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[PATL2]] | -0.59 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[IFNAR1]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.58 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[JMJD1C]] | -0.57 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ASH1L]] | -0.57 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[CUX1]] | -0.57 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.7, -29.0); signed map (-53.8, 2.6). **Vector** length 54.7, 7.95% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.50 to 11); *IRE1alpha activates chaperones* (reactome, mean cos +0.51 to 7); *unfolded protein response* (hallmark, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +0.7 | +2.5 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | +0.6 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -3.0 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.6 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | misato family member 2, pseudogene |
| Locus type | pseudogene |
| Location | 1q22 — chr1:155,745,829-155,750,137 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | ; previously MSTO2 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26329) · Entrez [100129405](https://www.ncbi.nlm.nih.gov/gene/100129405) · Ensembl [ENSG00000203761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203761)

## Data

Gene col 12786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12786); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12786]; `tensor/DDL_lfc|DDL_z.npy` [12786]; `embed/gene_vectors.npy` [12786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12786 or target_col == 12786). Every well: [[MSTO2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSTO2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
