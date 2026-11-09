---
symbol: "SP2-AS1"
type: "gene"
col: 13964
ensembl_id: "ENSG00000234494"
name: "SP2 antisense RNA 1"
location: "17q21.32"
module: 5
arm: "+"
pooled_cpm: 5.01
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SP2-AS1

*SP2 antisense RNA 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.12× (z +9.0, q 2e-16, up in 6 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.34× (z +3.7, q 0.030, up in 9 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.628× (z -5.7, q 5e-06, down in 17 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.216×, HT-29 0.246×; ⚠ cell-cycle shift, explains ~80% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.0546×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.114×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (J82 0.0832×); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0814×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC4]] (+0.70, fdr 7e-06), [[MRTO4]] (+0.67, fdr 7e-06), [[ALG8]] (+0.67, fdr 1e-05); moves opposite to [[PJA2]] (-0.55, fdr 2e-05), [[AAMDC]] (-0.55, fdr 3e-05), [[GNAI2]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +9.0 | 2e-16 | 6/9 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +7.4 | 3e-11 | 12/23 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +6.0 | 5e-07 | 6/14 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.9 | 6e-07 | 8/24 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.030 | 9/44 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.036 | 8/45 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +3.4 | 0.063 | 11/39 (NCI-H2347, HOP62, …) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.11 | 3/44 (KATO III, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | 1.61× | +3.1 | 0.11 | 2/38 (HEC-1-A, NCI-H1573) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.28× | +3.1 | 0.11 | 1/44 (NCI-H2347) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13964.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.216×, HT-29 0.246×; ⚠ cell-cycle shift, explains ~80% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.0546×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.114×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (J82 0.0832×); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0814×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.628×** | -5.7 | 5e-06 | 17/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.665×** | -5.0 | 1e-04 | 12/44 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 0.834× | -3.2 | 0.22 | 17/38 (LoVo, HT-29, …) | top dose only | composition shift |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.769× | -3.1 | 0.22 | 5/44 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | 0.766× | -3.1 | 0.22 | 5/43 (HOP62, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.49 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -11.3) ⚠ cell-cycle shift, explains ~80% of this change |
| [[HT-29 (line)]] | alt | 6.82 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -8.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[J82 (line)]] | alt | 4.27 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0832× (z -9.7) |
| [[KATO III (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0546× (z -14.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 4.26 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0814× (z -8.8) |
| [[SW1417 (line)]] | alt | 4.81 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.101× (z -9.0) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC4]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ALG8]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[WDR4]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[METAP1D]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[DHX37]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PVT1]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MRM1]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[UTP20]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TCERG1]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ZP3]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[HMGA1P4]] | +0.62 | +0.59 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AAMDC]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[GNAI2]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[PGM2L1]] | -0.54 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[LGALS1]] | -0.53 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[ARL3]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.53 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[PLEKHH3]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RNASE4]] | -0.52 | -0.50 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.0, -34.4); signed map (-0.3, -46.7). **Vector** length 47.6, 5.27% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.52 to 13); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +7.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +3.7 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.0 | -0.8 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.32 — chr17:47,897,330-47,941,410 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SP2-DT |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51341) · Entrez [100506325](https://www.ncbi.nlm.nih.gov/gene/100506325) · Ensembl [ENSG00000234494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234494)

## Data

Gene col 13964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13964); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13964]; `tensor/DDL_lfc|DDL_z.npy` [13964]; `embed/gene_vectors.npy` [13964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13964 or target_col == 13964). Every well: [[SP2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SP2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
