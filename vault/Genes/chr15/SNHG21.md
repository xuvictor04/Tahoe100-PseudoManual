---
symbol: "SNHG21"
type: "gene"
col: 14725
ensembl_id: "ENSG00000250988"
name: "small nucleolar RNA host gene 21"
location: "15q25.2"
module: 179
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# SNHG21

*small nucleolar RNA host gene 21* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.92× (z +11.7, q 8e-29, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.29× (z +7.4, q 3e-11, up in 15 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sodium Salicylate (drug)]] 0.05 µM in 1 line (SHP-77 0.0757×); [[LY2090314 (drug)]] 0.05 µM in 1 line (SHP-77 0.0752×); [[Pralsetinib (drug)]] 0.05 µM in 1 line (SHP-77 0.0784×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KHDC4]] (+0.64, fdr 7e-06), [[CDC26]] (+0.63, fdr 1e-05), [[C1orf52]] (+0.63, fdr 1e-05); moves opposite to [[CUX1]] (-0.63, fdr 1e-05), [[LRRC37A2]] (-0.58, fdr 3e-05), [[SYNE2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.92×** | +11.7 | 8e-29 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +8.6 | 2e-15 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +8.1 | 1e-13 | 6/10 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +7.4 | 3e-11 | 15/38 (HCT15, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.24×** | +6.7 | 2e-09 | 18/36 (KATO III, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +6.6 | 4e-09 | 9/43 (PANC-1, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.03×** | +6.3 | 3e-08 | 20/45 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.84×** | +5.4 | 4e-06 | 15/44 (NCI-H23, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.4 | 4e-06 | 8/11 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.8 | 9e-05 | 7/30 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.79×** | +4.8 | 9e-05 | 8/28 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.68×** | +4.6 | 2e-04 | 9/44 (A-172, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +4.2 | 0.001 | 1/15 (NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +3.9 | 0.003 | 1/45 (COLO 205) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.020 | 3/39 (A498, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +3.2 | 0.049 | 2/20 (NCI-H460, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.049 | 7/43 (NCI-H1573, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sodium Salicylate (drug)]] 0.05 µM in 1 line (SHP-77 0.0757×); [[LY2090314 (drug)]] 0.05 µM in 1 line (SHP-77 0.0752×); [[Pralsetinib (drug)]] 0.05 µM in 1 line (SHP-77 0.0784×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.695× | -3.3 | 0.65 | 8/43 (HS-578T, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 5.17 | 0 | 3 | — | [[Sodium Salicylate (drug)]] 0.05 µM 0.0757× (z -9.1) |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHDC4]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CDC26]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[C1orf52]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[DDN-AS1]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SGSM3]] | +0.62 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[NAT9]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RNF121]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZNF384]] | +0.59 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[SYCE1L]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CRYBB2P1]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ZNF526]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[AMPD2]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUX1]] | -0.63 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[LRRC37A2]] | -0.58 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SYNE2]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SETD2]] | -0.55 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[KTN1]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ROCK2]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NUCKS1]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SLK]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[STXBP3]] | -0.52 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SCAF11]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[EEA1]] | -0.51 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TIA1]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (7.4, -24.6); signed map (-46.5, 6.8). **Vector** length 39.4, 3.96% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +3.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[XRK3F2 (drug)]] 5 µM |  | -0.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 21 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q25.2 — chr15:82,750,545-82,757,738 (+) |
| Ensembl biotype | lncRNA |
| Also known as | SCARNA15HG, FSD2-AS1, RP11-752G15.6 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100505616](https://www.ncbi.nlm.nih.gov/gene/100505616):

> Predicted to be involved in RNA processing. Predicted to be located in Cajal body and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:50284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50284) · Entrez [100505616](https://www.ncbi.nlm.nih.gov/gene/100505616) · Ensembl [ENSG00000250988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250988)

## Data

Gene col 14725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14725); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14725]; `tensor/DDL_lfc|DDL_z.npy` [14725]; `embed/gene_vectors.npy` [14725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14725 or target_col == 14725). Every well: [[SNHG21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
