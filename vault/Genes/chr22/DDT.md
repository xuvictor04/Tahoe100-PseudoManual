---
symbol: "DDT"
type: "gene"
col: 1837
ensembl_id: "ENSG00000099977"
name: "D-dopachrome tautomerase"
location: "22q11.23"
module: 48
arm: "+"
pooled_cpm: 28.05
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# DDT

*D-dopachrome tautomerase* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.21× (z +5.7, q 5e-06, up in 39 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.526× (z -5.8, q 3e-06, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VKORC1]] (+0.79, fdr 7e-06), [[OST4]] (+0.78, fdr 7e-06), [[NDUFA2]] (+0.76, fdr 1e-05); moves opposite to [[EWSR1]] (-0.72, fdr 7e-06), [[SFPQ]] (-0.66, fdr 1e-05), [[SRSF1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.21×** | +5.7 | 5e-06 | 39/43 (KATO III, A498, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.27×** | +4.6 | 0.001 | 31/35 (KATO III, A549, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **2.00×** | +4.5 | 0.002 | 33/45 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | 1.71× | +3.2 | 0.19 | 23/38 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.526×** | -5.8 | 3e-06 | 35/47 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -4.4 | 0.003 | 32/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.305×** | -3.7 | 0.047 | 37/45 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.372× | -3.0 | 0.30 | 30/46 (SNU-1, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.595× | -3.0 | 0.30 | 28/48 (SW480, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 58.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.0) |
| [[RKO (line)]] | wt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.6) |
| [[SHP-77 (line)]] | alt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.8) |
| [[A-172 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[OST4]] | +0.78 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.76 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[COX6A1]] | +0.75 | +0.69 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[ROMO1]] | +0.75 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[FAU]] | +0.74 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[SF3B5]] ⚠ | +0.73 | +0.53 / +0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIF]] | +0.73 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[UBL5]] | +0.72 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.72 | +0.56 / +0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRPT1]] | +0.71 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[BBLN]] | +0.71 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RNF181]] | +0.71 | +0.38 / +0.79 | both halves | 7e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.72 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.66 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.66 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.64 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[NRAS]] | -0.64 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[U2AF2]] | -0.63 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[ANKRD40]] | -0.61 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.9, -21.2); signed map (-34.1, 10.5). **Vector** length 68.3, 23.1% of its response variance represented; |z| ≥ 3 in 393 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.59 to 31); *Respiratory electron transport* (reactome, mean cos +0.58 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.60 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | -1.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -5.7 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -5.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -4.5 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | D-dopachrome tautomerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:23,970,542-23,980,525 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DDCT, MIF2, MIF-2, D-DT |
| Gene groups (HGNC) | MIF family; Decarboxylases |
| Hallmark sets | XENOBIOTIC_METABOLISM, ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P30046](https://www.uniprot.org/uniprotkb/P30046) (D-dopachrome decarboxylase):

> Tautomerization of D-dopachrome with decarboxylation to give 5,6-dihydroxyindole (DHI).

**Summary**, from NCBI Gene [1652](https://www.ncbi.nlm.nih.gov/gene/1652):

> D-dopachrome tautomerase converts D-dopachrome into 5,6-dihydroxyindole. The DDT gene is related to the migration inhibitory factor (MIF) in terms of sequence, enzyme activity, and gene structure. DDT and MIF are closely linked on chromosome 22. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2732) · Entrez [1652](https://www.ncbi.nlm.nih.gov/gene/1652) · UniProt [P30046](https://www.uniprot.org/uniprotkb/P30046) · Ensembl [ENSG00000099977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099977)

## Data

Gene col 1837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1837); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1837]; `tensor/DDL_lfc|DDL_z.npy` [1837]; `embed/gene_vectors.npy` [1837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1837 or target_col == 1837). Every well: [[DDT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
