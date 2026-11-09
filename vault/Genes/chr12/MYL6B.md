---
symbol: "MYL6B"
type: "gene"
col: 12214
ensembl_id: "ENSG00000196465"
name: "myosin light chain 6B"
location: "12q13.2"
module: 21
arm: "+"
pooled_cpm: 13.53
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MYL6B

*myosin light chain 6B* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.80× (z +10.5, q 4e-23, up in 35 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +6.8, q 2e-09, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.576× (z -5.6, q 1e-05, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBOX5-AS1]] (+0.67, fdr 1e-05), [[HEXA]] (+0.66, fdr 1e-05), [[DNASE2]] (+0.64, fdr 1e-05); moves opposite to [[CEP83]] (-0.59, fdr 1e-05), [[SMC6]] (-0.58, fdr 1e-05), [[DNMT1]] (-0.58, fdr 2e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +10.5 | 4e-23 | 35/38 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.6 | 2e-19 | 19/24 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.8 | 2e-09 | 23/45 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +6.5 | 1e-08 | 29/33 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +5.5 | 4e-06 | 36/46 (LoVo, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.6 | 4e-04 | 23/42 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 24/47 (Hs 766T, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +4.1 | 0.003 | 21/42 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 1.37× | +3.1 | 0.12 | 13/46 (HepG2/C3A, HOP62, …) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.37× | +3.1 | 0.13 | 8/45 (A498, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12214.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -5.6 | 1e-05 | 33/45 (A-427, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.697×** | -5.2 | 6e-05 | 28/46 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.705×** | -3.6 | 0.070 | 18/45 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.729× | -3.1 | 0.28 | 14/46 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.9) |
| [[A498 (line)]] | wt | 11.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +8.9) | — |
| [[A-172 (line)]] | wt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -12.3) |
| [[PANC-1 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 22.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.180× (z -9.4) |
| [[A549 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBOX5-AS1]] | +0.67 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[HEXA]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[DNASE2]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CNGB3]] | +0.64 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[UBE4B]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LRRC37A16P]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PTRHD1]] ⚠ | +0.63 | +0.62 / +0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TSC22D4]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SPNS1]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[RSL1D1-DT]] | +0.61 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[CCDC115]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DCAF5]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[GCNT7]] | +0.60 | +0.39 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP83]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SMC6]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[DNMT1]] | -0.58 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CTPS1]] | -0.55 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[SMC1A]] | -0.55 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[PWP2]] | -0.55 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[EEFSEC]] | -0.54 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[CMSS1]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PPM1G]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.6, -16.5); signed map (-21.4, 3.1). **Vector** length 57.3, 10.1% of its response variance represented; |z| ≥ 3 in 638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.7 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +5.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -1.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.5 | -0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.1 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:56,152,256-56,159,647 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLC1SA |
| Gene groups (HGNC) | Myosin light chains, class 1 |
| Hallmark sets | MYOGENESIS |
| Reactome | 2 pathways, smallest: Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P14649](https://www.uniprot.org/uniprotkb/P14649) (Myosin light chain 6B):

> Regulatory light chain of myosin. Does not bind calcium.

**Summary**, from NCBI Gene [140465](https://www.ncbi.nlm.nih.gov/gene/140465):

> Myosin is a hexameric ATPase cellular motor protein. It is composed of two heavy chains, two nonphosphorylatable alkali light chains, and two phosphorylatable regulatory light chains. This gene encodes a myosin alkali light chain expressed in both slow-twitch skeletal muscle and in nonmuscle tissue. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:29823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29823) · Entrez [140465](https://www.ncbi.nlm.nih.gov/gene/140465) · UniProt [P14649](https://www.uniprot.org/uniprotkb/P14649) · Ensembl [ENSG00000196465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196465)

## Data

Gene col 12214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12214); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12214]; `tensor/DDL_lfc|DDL_z.npy` [12214]; `embed/gene_vectors.npy` [12214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12214 or target_col == 12214). Every well: [[MYL6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYL6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
