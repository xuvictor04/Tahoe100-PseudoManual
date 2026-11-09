---
symbol: "CLN8-AS1"
type: "gene"
col: 14852
ensembl_id: "ENSG00000253982"
name: "CLN8 antisense RNA 1"
location: "8p23.3"
module: 24
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# CLN8-AS1

*CLN8 antisense RNA 1* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.90× (z +10.2, q 8e-22, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.78× (z +6.4, q 2e-08, up in 13 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.480× (z -5.7, q 6e-06, down in 21 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf1]] (+0.71, fdr 1e-05), [[PITPNA-AS1]] (+0.69, fdr 1e-05), [[ZFAND2A-DT]] (+0.68, fdr 2e-05); moves opposite to [[HNRNPAB]] (-0.63, fdr 2e-05), [[NUP188]] (-0.61, fdr 5e-05), [[PSME3]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +10.2 | 8e-22 | 2/2 (NCI-H2347, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +9.5 | 4e-19 | 9/13 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +7.1 | 3e-10 | 3/3 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +6.4 | 2e-08 | 13/42 (NCI-H460, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.13×** | +5.9 | 4e-07 | 6/14 (NCI-H2030, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.05×** | +3.7 | 0.019 | 5/22 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.037 | 3/25 (A549, RPMI-7951, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.5 | 0.037 | 2/10 (NCI-H460, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.074 | 4/37 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.100 | 1/19 (HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.1 | 0.100 | 1/3 (HEC-1-A) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -5.7 | 6e-06 | 21/45 (HCT15, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.486×** | -5.6 | 6e-06 | 20/39 (BT-474, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.563×** | -4.2 | 0.005 | 12/40 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.592×** | -4.1 | 0.007 | 15/44 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.626×** | -3.6 | 0.031 | 11/36 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.736×** | -3.4 | 0.075 | 19/31 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.92 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.55× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 3.02 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0916× (z -8.5) |
| [[A-172 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.945 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.623 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.802 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf1]] | +0.71 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[PITPNA-AS1]] | +0.69 | +0.49 / +0.70 | both halves | 1e-05 | same gene group |
| [[ZFAND2A-DT]] | +0.68 | +0.46 / +0.72 | both halves | 2e-05 |  |
| [[RAB9A]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SPACA9]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[AKAP1-DT]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | +0.64 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[EXOC3-AS1]] | +0.64 | +0.40 / +0.73 | both halves | 5e-05 | same gene group |
| [[TP53TG1]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.64 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[EID2B]] | +0.62 | +0.42 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.63 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[NUP188]] | -0.61 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[PSME3]] | -0.59 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[CTPS1]] | -0.58 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[GCN1]] | -0.57 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[NOLC1]] | -0.57 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[SMC1A]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.57 | -0.46 / -0.50 | both halves | 2e-05 | same gene group |
| [[MCM8]] | -0.55 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[UBE2G2]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PRPS2]] | -0.54 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[ELK4]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.9, -16.8); signed map (-9.0, 1.0). **Vector** length 32.4, 3.14% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.2 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +3.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.8 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -5.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.1 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.8 | -4.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.7 | -2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.7 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -0.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | CLN8 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p23.3 — chr8:1,761,054-1,764,508 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55523) · Entrez [101927752](https://www.ncbi.nlm.nih.gov/gene/101927752) · Ensembl [ENSG00000253982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253982)

## Data

Gene col 14852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14852); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14852]; `tensor/DDL_lfc|DDL_z.npy` [14852]; `embed/gene_vectors.npy` [14852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14852 or target_col == 14852). Every well: [[CLN8-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLN8-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
