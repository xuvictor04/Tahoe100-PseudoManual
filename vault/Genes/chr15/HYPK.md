---
symbol: "HYPK"
type: "gene"
col: 14298
ensembl_id: "ENSG00000242028"
name: "huntingtin interacting protein K"
location: "15q15.3"
module: 179
arm: "+"
pooled_cpm: 8.51
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# HYPK

*huntingtin interacting protein K* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +6.8, q 8e-09, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.441× (z -8.0, q 1e-12, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R32]] (+0.77, fdr 7e-06), [[CDC26]] (+0.72, fdr 7e-06), [[TMED7-TICAM2]] (+0.71, fdr 7e-06); moves opposite to [[CEP41]] (-0.57, fdr 1e-05), [[SLX4IP]] (-0.57, fdr 1e-05), [[WDR7]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.8 | 8e-09 | 23/41 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +6.2 | 2e-07 | 29/44 (HT-29, SNU-423, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **2.01×** | +3.6 | 0.070 | 8/45 (A498, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.41× | +3.3 | 0.12 | 12/45 (A549, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.441×** | -8.0 | 1e-12 | 34/46 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.432×** | -7.8 | 1e-12 | 32/46 (NCI-H2030, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.544×** | -5.9 | 6e-07 | 21/33 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.535×** | -5.9 | 7e-07 | 24/44 (LoVo, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.560×** | -5.4 | 7e-06 | 15/16 (A498, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.622×** | -4.6 | 4e-04 | 21/47 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.640×** | -4.3 | 1e-03 | 19/46 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -4.3 | 1e-03 | 21/42 (NCI-H2030, H4, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.644×** | -4.3 | 0.001 | 21/46 (LS 180, H4, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.661×** | -4.0 | 0.003 | 17/44 (HS-578T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.661×** | -4.0 | 0.003 | 18/46 (A498, COLO 205, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.669×** | -3.9 | 0.004 | 18/47 (hTERT-HPNE, NCI-H2030, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.763×** | -3.7 | 0.009 | 21/42 (A549, CFPAC-1, …) | all doses, flat | composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.499×** | -3.5 | 0.016 | 14/38 (SW1417, A549, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.695×** | -3.5 | 0.016 | 11/46 (NCI-H1792, KATO III, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.697×** | -3.5 | 0.016 | 17/45 (HS-578T, SW 900, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 22.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0412× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.187× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.123× (z -8.9) |
| [[A-427 (line)]] | wt | 4.51 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0764× (z -9.0) |
| [[A498 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[A549 (line)]] | wt | 5.39 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.113× (z -9.1) |
| [[BT-474 (line)]] | alt | 7.36 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0876× (z -8.6) |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0547× (z -11.0) |
| [[Hs 766T (line)]] | wt | 6.80 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 0.5 µM 0.0978× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0883× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0969× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW480 (line)]] | alt | 8.25 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.194× (z -9.1) |
| [[A-172 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R32]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[CDC26]] | +0.72 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[TMED7-TICAM2]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[PGM3]] | +0.69 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[BNIPL]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TICAM2]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.67 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[BET1L]] | +0.67 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[SLC39A7]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CLEC4A]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[RNF139-DT]] | +0.66 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[TNXB]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP41]] | -0.57 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[WDR7]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (17.5, -28.7); signed map (-46.4, 10.6). **Vector** length 85.7, 16.6% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.7 | -2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -8.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.9 | -4.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.5 | -3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | huntingtin interacting protein K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,796,142-43,804,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC136, FLJ20431; previously C15orf63 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX55](https://www.uniprot.org/uniprotkb/Q9NX55) (Huntingtin-interacting protein K):

> Component of several N-terminal acetyltransferase complexes. Inhibits the N-terminal acetylation activity of the N-terminal acetyltransferase NAA10-NAA15 complex (also called the NatA complex). Has chaperone-like activity preventing polyglutamine (polyQ) aggregation of HTT in neuronal cells probably while associated with the NatA complex. May play a role in the NatA complex-mediated N-terminal acetylation of PCNP.

**Summary**, from NCBI Gene [25764](https://www.ncbi.nlm.nih.gov/gene/25764):

> Enables protein folding chaperone. Involved in negative regulation of apoptotic process and protein stabilization. Located in cytoplasm and nucleoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18418) · Entrez [25764](https://www.ncbi.nlm.nih.gov/gene/25764) · UniProt [Q9NX55](https://www.uniprot.org/uniprotkb/Q9NX55) · Ensembl [ENSG00000242028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242028)

## Data

Gene col 14298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14298); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14298]; `tensor/DDL_lfc|DDL_z.npy` [14298]; `embed/gene_vectors.npy` [14298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14298 or target_col == 14298). Every well: [[HYPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
