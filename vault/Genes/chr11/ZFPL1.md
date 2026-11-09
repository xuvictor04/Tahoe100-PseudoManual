---
symbol: "ZFPL1"
type: "gene"
col: 8497
ensembl_id: "ENSG00000162300"
name: "zinc finger protein like 1"
location: "11q13.1"
module: 40
arm: "+"
pooled_cpm: 14.47
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ZFPL1

*zinc finger protein like 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.43× (z +4.3, q 0.008, up in 18 of 44 measured lines) ⚠ transcription drop.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.551× (z -9.4, q 3e-18, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIPF2]] (+0.77, fdr 7e-06), [[GPR107]] (+0.70, fdr 7e-06), [[IFT20]] (+0.69, fdr 7e-06); moves opposite to [[ROCK2]] (-0.63, fdr 7e-06), [[CDK6]] (-0.61, fdr 1e-05), [[RUVBL1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.3 | 0.008 | 18/44 (hTERT-HPNE, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.8 | 0.047 | 1/48 (HOP62) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.44 | 13/44 (SHP-77, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.551×** | -9.4 | 3e-18 | 35/47 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.479×** | -8.6 | 2e-15 | 38/47 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.278×** | -8.1 | 9e-14 | 35/48 (NCI-H2347, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.535×** | -7.6 | 4e-12 | 35/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.561×** | -7.0 | 3e-10 | 33/47 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.340×** | -6.8 | 7e-10 | 33/43 (NCI-H2347, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -6.5 | 8e-09 | 25/44 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.604×** | -6.1 | 6e-08 | 29/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.608×** | -6.0 | 9e-08 | 32/48 (HCT15, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.693×** | -5.9 | 2e-07 | 31/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -5.0 | 3e-05 | 25/47 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.677×** | -4.5 | 4e-04 | 22/47 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.697×** | -4.4 | 5e-04 | 16/46 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.716×** | -4.1 | 0.002 | 19/48 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.573×** | -3.5 | 0.015 | 12/48 (AsPC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -3.1 | 0.066 | 13/48 (SNU-423, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.776×** | -3.1 | 0.068 | 10/46 (SW 900, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 8.92 | 0 | 3 | — | [[Ferulic acid (drug)]] 5 µM 0.0562× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.0716× (z -10.5) |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.367× (z -8.7) |
| [[C32 (line)]] | wt | 9.00 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -8.5) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.6) |
| [[HS-578T (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -10.2) |
| [[J82 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 9.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.0) |
| [[A-172 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF2]] | +0.77 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[GPR107]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[IFT20]] | +0.69 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[BET1L]] | +0.68 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[TULP3]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[RINT1]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.67 | +0.70 / +0.67 | both halves | 7e-06 | STRING 608 |
| [[SYVN1]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 | same gene group; ⚠ same locus (33.4 kb: neighbours can correlate without regulation) |
| [[PLPP5]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SDHAP1-1]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK2]] | -0.63 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[CDK6]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.60 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[RAB10]] | -0.58 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[TRIM44]] | -0.58 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.58 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[SERBP1]] | -0.57 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[C1QBP]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (9.4, -34.4); signed map (-48.0, 11.4). **Vector** length 78.4, 15.7% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +1.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.4 | -8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,084,210-65,088,398 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D11S750, MCG4 |
| Gene groups (HGNC) | Zinc fingers; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95159](https://www.uniprot.org/uniprotkb/O95159) (Zinc finger protein-like 1):

> Required for cis-Golgi integrity and efficient ER to Golgi transport. Involved in the maintenance of the integrity of the cis-Golgi, possibly via its interaction with GOLGA2/GM130.

**Summary**, from NCBI Gene [7542](https://www.ncbi.nlm.nih.gov/gene/7542):

> Predicted to enable DNA binding activity and zinc ion binding activity. Predicted to be involved in regulation of DNA-templated transcription. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12868) · Entrez [7542](https://www.ncbi.nlm.nih.gov/gene/7542) · UniProt [O95159](https://www.uniprot.org/uniprotkb/O95159) · Ensembl [ENSG00000162300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162300)

## Data

Gene col 8497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8497); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8497]; `tensor/DDL_lfc|DDL_z.npy` [8497]; `embed/gene_vectors.npy` [8497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8497 or target_col == 8497). Every well: [[ZFPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
