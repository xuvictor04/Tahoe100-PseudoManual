---
symbol: "HSD17B2-AS1"
type: "gene"
col: 15333
ensembl_id: "ENSG00000261235"
name: "HSD17B2 antisense RNA 1"
location: "16q23.3"
module: 47
arm: "+"
pooled_cpm: 3.56
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# HSD17B2-AS1

*HSD17B2 antisense RNA 1* — 16q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.80× (z +10.0, q 1e-20, up in 26 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.475× (z -7.2, q 2e-10, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBA8]] (+0.62, fdr 1e-05), [[BAAT]] (+0.60, fdr 7e-06), [[MTNR1A]] (+0.58, fdr 1e-05); moves opposite to [[GINM1]] (-0.56, fdr 3e-05), [[LRP11]] (-0.53, fdr 3e-05), [[GXYLT2]] (-0.49, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.80×** | +10.0 | 1e-20 | 26/41 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +9.8 | 5e-20 | 9/18 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +9.1 | 2e-17 | 1/4 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +7.5 | 1e-11 | 4/7 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +7.3 | 3e-11 | 9/19 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +6.5 | 6e-09 | 12/35 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +5.9 | 3e-07 | 9/44 (COLO 205, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.9 | 6e-05 | 9/33 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.003 | 5/47 (SW480, RKO, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.22×** | +4.0 | 0.003 | 3/30 (COLO 205, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +3.9 | 0.004 | 2/5 (NCI-H460, NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.007 | 7/42 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.98×** | +3.5 | 0.024 | 1/24 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +3.2 | 0.048 | 9/44 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.070 | 8/42 (LoVo, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15333.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -7.2 | 2e-10 | 24/45 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -6.1 | 3e-07 | 21/43 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -5.6 | 5e-06 | 23/44 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -5.1 | 4e-05 | 15/33 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.733×** | -3.3 | 0.097 | 9/45 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.715×** | -3.3 | 0.097 | 6/45 (HCT15, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.718× | -3.1 | 0.18 | 8/37 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.29 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0317× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0568× (z -9.2) |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0891× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[HEC-1-A (line)]] | alt | 3.49 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0807× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 2.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +9.9) | — |
| [[RKO (line)]] | wt | 7.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -8.9) |
| [[A-427 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBA8]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[BAAT]] | +0.60 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MTNR1A]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ASAH2B]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CFAP161]] | +0.56 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[EEF1AKMT1]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 | same gene group |
| [[SLC2A9]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MYH3]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LINC00486]] | +0.55 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CRACR2A]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SPON2]] | +0.54 | +0.59 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GINM1]] | -0.56 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[LRP11]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[GXYLT2]] | -0.49 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[NMT2]] | -0.48 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[TXNDC16]] | -0.48 | -0.23 / -0.39 | both halves | 5e-04 |  |
| [[FBXL20]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PRKRA]] | -0.47 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[MTM1]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, -11.7); signed map (17.6, 3.9). **Vector** length 56.4, 7.30% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +9.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -7.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | HSD17B2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q23.3 — chr16:82,044,336-82,139,631 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-510J16.5, AS-HSD17beta2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56281) · Entrez [105371363](https://www.ncbi.nlm.nih.gov/gene/105371363) · Ensembl [ENSG00000261235](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261235)

## Data

Gene col 15333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15333); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15333]; `tensor/DDL_lfc|DDL_z.npy` [15333]; `embed/gene_vectors.npy` [15333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15333 or target_col == 15333). Every well: [[HSD17B2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD17B2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
