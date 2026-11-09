---
symbol: "CAPN10-DT"
type: "gene"
col: 15314
ensembl_id: "ENSG00000260942"
name: "CAPN10 divergent transcript"
location: "2q37.3"
module: 15
arm: "+"
pooled_cpm: 2.23
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CAPN10-DT

*CAPN10 divergent transcript* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.16× (z +13.9, q 7e-41, up in 32 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.433× (z -6.9, q 4e-09, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR762HG]] (+0.75, fdr 7e-06), [[LINC00115]] (+0.75, fdr 7e-06), [[TAF11]] (+0.74, fdr 7e-06); moves opposite to [[ROCK2]] (-0.57, fdr 1e-05), [[WDR7]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.16×** | +13.9 | 7e-41 | 32/38 (SW480, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +11.0 | 1e-25 | 27/32 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.63×** | +10.4 | 3e-23 | 8/10 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +6.9 | 7e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +6.2 | 5e-08 | 10/44 (PANC-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.2 | 2e-05 | 7/24 (NCI-H23, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +4.7 | 3e-04 | 2/3 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.4 | 8e-04 | 3/12 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +3.7 | 0.012 | 6/38 (PANC-1, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.012 | 6/27 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.4 | 0.033 | 8/47 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.033 | 1/23 (SW1417) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.2 | 0.049 | 1/11 (SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.2 | 0.049 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.049 | 10/39 (KATO III, AsPC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.433×** | -6.9 | 4e-09 | 22/37 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.569×** | -4.8 | 3e-04 | 14/44 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.674×** | -4.8 | 3e-04 | 19/34 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.600×** | -4.4 | 0.002 | 8/42 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.618×** | -4.0 | 0.008 | 10/37 (PANC-1, LoVo, …) | top dose only |  |
| [[Afatinib (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.085 | 2/47 (PANC-1, NCI-H2347) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.86 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -8.5) |
| [[A-172 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.683 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR762HG]] | +0.75 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[LINC00115]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TAF11]] | +0.74 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[CDC26]] | +0.73 | +0.56 / +0.79 | both halves | 1e-05 |  |
| [[GOT1-DT]] | +0.73 | +0.46 / +0.77 | both halves | 3e-05 | same gene group |
| [[CCNY-AS1]] | +0.72 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[GLUD1P3]] | +0.72 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[VPS13B-DT]] | +0.71 | +0.51 / +0.74 | both halves | 1e-05 | same gene group |
| [[SEPTIN1]] | +0.71 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[C12orf73]] | +0.68 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[PCGF3-AS1]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.67 | +0.62 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK2]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[WDR7]] | -0.56 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.2, 23.5); signed map (1.7, -0.4). **Vector** length 53.7, 7.36% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +10.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | CAPN10 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q37.3 — chr2:240,582,700-240,586,699 (-) |
| Ensembl biotype | lncRNA |
| Also known as | locus959; previously CAPN10-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48839) · Entrez [101752400](https://www.ncbi.nlm.nih.gov/gene/101752400) · Ensembl [ENSG00000260942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260942)

## Data

Gene col 15314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15314); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15314]; `tensor/DDL_lfc|DDL_z.npy` [15314]; `embed/gene_vectors.npy` [15314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15314 or target_col == 15314). Every well: [[CAPN10-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN10-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
