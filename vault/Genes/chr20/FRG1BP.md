---
symbol: "FRG1BP"
type: "gene"
col: 7382
ensembl_id: "ENSG00000149531"
name: "FSHD region gene 1 family member B, pseudogene"
location: "20q11.1"
module: 17
arm: "+"
pooled_cpm: 8.43
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# FRG1BP

*FSHD region gene 1 family member B, pseudogene* — 20q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.84× (z +10.8, q 2e-24, up in 27 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.557× (z -7.4, q 1e-10, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRG1DP]] (+0.72, fdr 7e-06), [[KCTD18]] (+0.70, fdr 7e-06), [[TRUB1]] (+0.66, fdr 7e-06); moves opposite to [[SNRPB]] (-0.53, fdr 3e-05), [[DMPK]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.84×** | +10.8 | 2e-24 | 27/39 (SNU-423, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +8.2 | 5e-14 | 24/38 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +6.6 | 1e-08 | 20/39 (SK-MEL-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +6.5 | 1e-08 | 26/40 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +5.7 | 1e-06 | 17/33 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.3 | 9e-06 | 17/40 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +5.3 | 1e-05 | 17/39 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +4.4 | 7e-04 | 10/39 (NCI-H23, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 0.002 | 9/39 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +3.9 | 0.006 | 9/37 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.006 | 9/39 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.6 | 0.016 | 7/38 (A549, HT-29, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.018 | 9/36 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.5 | 0.022 | 5/15 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.28×** | +3.1 | 0.066 | 5/40 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.072 | 3/40 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.072 | 9/37 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.073 | 6/39 (KATO III, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7382.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.557×** | -7.4 | 1e-10 | 22/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.599×** | -6.5 | 3e-08 | 22/39 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.608×** | -6.3 | 7e-08 | 21/40 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -5.9 | 7e-07 | 20/35 (J82, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -5.4 | 9e-06 | 22/38 (SNU-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.3 | 0.002 | 7/41 (RKO, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.755×** | -3.5 | 0.032 | 12/38 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 7.14 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0559× (z -11.5) |
| [[J82 (line)]] | alt | 5.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0911× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 8.36 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0578× (z -8.7) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.895 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1DP]] | +0.72 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[KCTD18]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.66 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[PYROXD1]] | +0.66 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[BBS2]] | +0.62 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[FRG1GP]] | +0.62 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[BPNT1]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.61 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[TMEM128]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[METTL14]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MRS2]] | +0.60 | +0.46 / +0.71 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[DMPK]] | -0.49 | -0.36 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.7, 2.3); signed map (-24.4, -10.4). **Vector** length 59.3, 10.3% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.0 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +8.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.9 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | FSHD region gene 1 family member B, pseudogene |
| Locus type | pseudogene |
| Location | 20q11.1 — chr20:30,377,372-30,399,257 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | bA348I14.2; previously C20orf80, FRG1B |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:15792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15792) · Entrez [284802](https://www.ncbi.nlm.nih.gov/gene/284802) · Ensembl [ENSG00000149531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149531)

## Data

Gene col 7382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7382); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7382]; `tensor/DDL_lfc|DDL_z.npy` [7382]; `embed/gene_vectors.npy` [7382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7382 or target_col == 7382). Every well: [[FRG1BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
