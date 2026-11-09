---
symbol: "PSMG3-AS1"
type: "gene"
col: 13754
ensembl_id: "ENSG00000230487"
name: "PSMG3 antisense RNA 1"
location: "7p22.3"
module: 35
arm: "+"
pooled_cpm: 4.64
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PSMG3-AS1

*PSMG3 antisense RNA 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +10.7, q 1e-23, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.361× (z -9.4, q 3e-18, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PJVK]] (+0.77, fdr 7e-06), [[PPP1R3F]] (+0.73, fdr 9e-06), [[ZNF213-AS1]] (+0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +10.7 | 1e-23 | 33/40 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +8.1 | 2e-13 | 3/5 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.0 | 4e-10 | 14/26 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +5.5 | 6e-06 | 21/35 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +4.7 | 3e-04 | 14/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.002 | 19/40 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.3 | 0.002 | 4/9 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.003 | 13/43 (A-427, PANC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.006 | 5/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.011 | 10/46 (LoVo, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.6 | 0.019 | 6/25 (HS-578T, Hs 766T, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.11 | 9/44 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.361×** | -9.4 | 3e-18 | 33/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.429×** | -7.8 | 1e-12 | 34/46 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.485×** | -6.7 | 5e-09 | 26/37 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.560×** | -5.3 | 1e-05 | 23/46 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.589×** | -4.9 | 1e-04 | 21/45 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.646×** | -4.0 | 0.005 | 11/47 (PANC-1, BT-474, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.659×** | -3.8 | 0.010 | 12/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.692×** | -3.4 | 0.050 | 16/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.692×** | -3.3 | 0.071 | 14/28 (SW480, KATO III, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.715× | -3.1 | 0.11 | 14/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 4.87 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0556× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 6.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0565× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 5.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.45 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJVK]] | +0.77 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[PPP1R3F]] | +0.73 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[ZNF213-AS1]] | +0.73 | +0.70 / +0.59 | both halves | 7e-06 | same gene group |
| [[LRRC37A3]] | +0.72 | +0.78 / +0.40 | both halves | 5e-05 |  |
| [[SEPTIN7-DT]] | +0.72 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.72 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | +0.72 | +0.71 / +0.62 | both halves | 7e-06 | same gene group |
| [[CTBP1-DT]] | +0.72 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[ZCWPW1]] | +0.71 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[DDX19A-DT]] | +0.70 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[QRICH2]] | +0.70 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.70 | +0.71 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.3, 19.9); signed map (27.5, -5.4). **Vector** length 57.2, 7.93% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -9.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -4.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | PSMG3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p22.3 — chr7:1,570,073-1,589,626 (+) |
| Ensembl biotype | lncRNA |
| Also known as | KIAA1908 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q96PY0](https://www.uniprot.org/uniprotkb/Q96PY0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22230) · Entrez [114796](https://www.ncbi.nlm.nih.gov/gene/114796) · UniProt [Q96PY0](https://www.uniprot.org/uniprotkb/Q96PY0) · Ensembl [ENSG00000230487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230487)

## Data

Gene col 13754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13754); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13754]; `tensor/DDL_lfc|DDL_z.npy` [13754]; `embed/gene_vectors.npy` [13754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13754 or target_col == 13754). Every well: [[PSMG3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMG3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
