---
symbol: "ZNF587B"
type: "gene"
col: 15621
ensembl_id: "ENSG00000269343"
name: "zinc finger protein 587B"
location: "19q13.43"
module: 33
arm: "+"
pooled_cpm: 14.13
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ZNF587B

*zinc finger protein 587B* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.67× (z +4.8, q 0.001, up in 34 of 48 measured lines) ⚠ unreliable plate only.
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.541× (z -5.7, q 5e-06, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF587]] (+0.80, fdr 7e-06, ⚠ same locus), [[GCN1]] (+0.80, fdr 7e-06), [[LRRC59]] (+0.69, fdr 7e-06), [[TRNT1]] (+0.68, fdr 1e-05); moves opposite to [[ANKRD12]] (-0.67, fdr 7e-06), [[KMT2A]] (-0.62, fdr 1e-05), [[PIAS1]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +4.8 | 0.001 | 34/48 (SW480, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.541×** | -5.7 | 5e-06 | 33/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.562×** | -5.4 | 2e-05 | 32/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.592×** | -4.9 | 2e-04 | 29/47 (SW480, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.722×** | -4.3 | 0.002 | 25/47 (RKO, A498, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -3.7 | 0.021 | 23/44 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.683×** | -3.6 | 0.033 | 24/45 (H4, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.682×** | -3.4 | 0.045 | 20/47 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Bendamustine (drug)]] 5 µM |  | **0.690×** | -3.3 | 0.059 | 22/45 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.707×** | -3.3 | 0.071 | 17/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.710×** | -3.2 | 0.075 | 19/45 (SNU-423, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.722× | -3.1 | 0.12 | 17/45 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 16.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.1) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.4) |
| [[A498 (line)]] | wt | 26.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 29.8 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.05 µM 0.116× (z -9.2) |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0674× (z -8.7) |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~98% of this change |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -9.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H2347 (line)]] | alt | 9.12 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -8.6) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM 0.0703× (z -10.0) |
| [[SNU-423 (line)]] | alt | 6.59 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.110× (z -9.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.112× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~98% of this change |
| [[SW48 (line)]] | wt | 15.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -9.0) |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF587]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 | same gene group; ⚠ same locus (3.6 kb, same strand: neighbours can correlate without regulation) |
| [[GCN1]] | +0.80 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[LRRC59]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[TRNT1]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[DCAF13]] | +0.66 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[LIG3]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PUM3]] | +0.65 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[NOLC1]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[URB1]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SPTLC1]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[IPO4]] | +0.63 | +0.57 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD12]] | -0.67 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[KMT2A]] | -0.62 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[PIAS1]] | -0.62 | -0.32 / -0.68 | both halves | 1e-04 |  |
| [[RRAGC]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[RNF24]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[CCDC24]] | -0.58 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[IFI27L2]] | -0.58 | -0.31 / -0.67 | both halves | 2e-04 |  |
| [[GABARAP]] ⚠ | -0.57 | -0.47 / -0.54 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM205]] | -0.56 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[CERT1]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[CDKN2D]] | -0.55 | -0.31 / -0.67 | both halves | 2e-04 |  |
| [[ARID4A]] | -0.55 | -0.38 / -0.59 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.359). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.8, -28.1); signed map (-23.1, -43.9). **Vector** length 78.6, 15.8% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -3.8 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -3.2 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -3.1 | -3.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 587B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:57,819,721-57,846,238 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [E7ETH6](https://www.uniprot.org/uniprotkb/E7ETH6) (Zinc finger protein 587B):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [100293516](https://www.ncbi.nlm.nih.gov/gene/100293516):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37142) · Entrez [100293516](https://www.ncbi.nlm.nih.gov/gene/100293516) · UniProt [E7ETH6](https://www.uniprot.org/uniprotkb/E7ETH6) · Ensembl [ENSG00000269343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269343)

## Data

Gene col 15621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15621); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15621]; `tensor/DDL_lfc|DDL_z.npy` [15621]; `embed/gene_vectors.npy` [15621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15621 or target_col == 15621). Every well: [[ZNF587B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF587B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
