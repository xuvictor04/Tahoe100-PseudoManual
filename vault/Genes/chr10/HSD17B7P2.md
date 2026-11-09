---
symbol: "HSD17B7P2"
type: "gene"
col: 1786
ensembl_id: "ENSG00000099251"
name: "hydroxysteroid 17-beta dehydrogenase 7 pseudogene 2"
location: "10p11.1"
module: 86
arm: "+"
pooled_cpm: 3.05
n_lines_expressing: 45
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# HSD17B7P2

*hydroxysteroid 17-beta dehydrogenase 7 pseudogene 2* — 10p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.16× (z +9.2, q 2e-17, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.564× (z -4.9, q 5e-04, down in 21 of 41 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.577× (z -4.7, q 7e-04, down in 15 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD17B7]] (+0.83, fdr 7e-06), [[MSMO1]] (+0.75, fdr 7e-06), [[MVD]] (+0.72, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.55, fdr 1e-05), [[NIP7]] (-0.52, fdr 1e-05), [[CYREN]] (-0.52, fdr 3e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.16×** | +9.2 | 2e-17 | 23/41 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.84×** | +7.3 | 9e-11 | 25/41 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.55×** | +5.2 | 4e-05 | 7/41 (HT-29, RKO, …) | rises with dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.2 | 4e-05 | 6/23 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +5.0 | 6e-05 | 14/41 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +4.4 | 9e-04 | 9/38 (A-427, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.4 | 0.001 | 5/13 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.005 | 7/34 (HepG2/C3A, LOX-IMVI, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 0.5 µM |  | **1.57×** | +3.8 | 0.009 | 6/38 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +3.8 | 0.010 | 10/39 (SW1417, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.010 | 8/41 (BT-474, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.49×** | +3.2 | 0.071 | 11/37 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.081 | 8/42 (H4, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.564×** | -4.9 | 5e-04 | 21/41 (A-427, C32, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.577×** | -4.7 | 7e-04 | 15/40 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.577×** | -4.5 | 0.001 | 14/36 (PANC-1, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.613×** | -4.2 | 0.004 | 11/36 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.632×** | -3.8 | 0.018 | 12/38 (A549, NCI-H23, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.652×** | -3.7 | 0.020 | 7/41 (BT-474, AsPC-1, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.641×** | -3.7 | 0.020 | 10/36 (A-172, CFPAC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.671×** | -3.4 | 0.039 | 15/32 (HCT15, CFPAC-1, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 5 µM |  | **0.661×** | -3.4 | 0.039 | 6/33 (HOP62, A-427, …) | rises with dose | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.675×** | -3.4 | 0.041 | 13/42 (SW1417, SHP-77, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.772×** | -3.2 | 0.083 | 6/41 (C32, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.704× | -3.0 | 0.12 | 6/42 (NCI-H1792, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.66 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0590× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 4.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 2.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0812× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.973 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B7]] | +0.83 | +0.75 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[MSMO1]] | +0.75 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[MVD]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[FDPS]] | +0.72 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[FDFT1]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ERG28]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ACSS2]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[SCD]] | +0.66 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[HMGCR]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[STAM]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SREBF2]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[STARD4]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[NIP7]] | -0.52 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CYREN]] | -0.52 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[FJX1]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[CRK]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PPRC1]] | -0.51 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ZBTB38]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DOCK1]] | -0.50 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[REXO1]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[AGO2]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TNFRSF12A]] | -0.49 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CUX1]] | -0.49 | -0.37 / -0.54 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.0, -48.9); signed map (-53.7, 32.4). **Vector** length 58.9, 9.26% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.56 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.58 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.54 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +3.1 | +9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.6 | +3.2 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.4 | +7.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.6 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.6 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid 17-beta dehydrogenase 7 pseudogene 2 |
| Locus type | pseudogene |
| Location | 10p11.1 — chr10:38,356,455-38,378,107 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | HSD17B7, bA291L22.1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28120](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28120) · Entrez [158160](https://www.ncbi.nlm.nih.gov/gene/158160) · Ensembl [ENSG00000099251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099251)

## Data

Gene col 1786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1786); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1786]; `tensor/DDL_lfc|DDL_z.npy` [1786]; `embed/gene_vectors.npy` [1786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1786 or target_col == 1786). Every well: [[HSD17B7P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD17B7P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
