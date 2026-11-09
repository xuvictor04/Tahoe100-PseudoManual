---
symbol: "PHLDB3"
type: "gene"
col: 10726
ensembl_id: "ENSG00000176531"
name: "pleckstrin homology like domain family B member 3"
location: "19q13.31"
module: 3
arm: "+"
pooled_cpm: 17.72
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PHLDB3

*pleckstrin homology like domain family B member 3* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.36× (z +5.0, q 3e-04, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.737× (z -4.8, q 0.001, down in 13 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 0.5 µM: 0.782× (z -4.0, q 0.009, down in 12 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGPEP1]] (+0.68, fdr 7e-06), [[EML2]] (+0.62, fdr 1e-05), [[ATAT1]] (+0.58, fdr 1e-05); moves opposite to [[TBC1D5]] (-0.57, fdr 2e-05), [[FGD5-AS1]] (-0.57, fdr 1e-05), [[HNRNPK]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +5.0 | 3e-04 | 22/46 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.6 | 0.001 | 19/42 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.050 | 13/44 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.23× | +3.3 | 0.15 | 11/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 1.21× | +3.1 | 0.20 | 12/47 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.737×** | -4.8 | 0.001 | 13/30 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -4.4 | 0.002 | 19/43 (SHP-77, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **0.780×** | -4.0 | 0.009 | 20/40 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.782×** | -4.0 | 0.009 | 12/46 (NCI-H460, AsPC-1, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -3.6 | 0.040 | 18/47 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.790×** | -3.5 | 0.040 | 16/34 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.798×** | -3.4 | 0.046 | 9/46 (C32, SW1417, …) | inconsistent across doses |  |
| [[Furosemide (drug)]] 0.5 µM |  | **0.816×** | -3.3 | 0.068 | 9/46 (HCT15, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.824× | -3.0 | 0.15 | 12/46 (HS-578T, A549, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.824× | -3.0 | 0.15 | 10/45 (NCI-H460, CHP-212, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 21.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0594× (z -9.8) |
| [[KATO III (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -12.0) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -8.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -8.9) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.240× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -13.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[A-172 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGPEP1]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[EML2]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ATAT1]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[GIPR]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ZNF816-ZNF321P]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LINC00674]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[GPR157]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[YPEL3]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHM1P1]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[ATG2A]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[KCNK6]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D5]] | -0.57 | -0.49 / -0.51 | both halves | 2e-05 |  |
| [[FGD5-AS1]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[WNK1]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[EIF4G2]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TRIM44]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PARD3B]] | -0.52 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[B3GALNT1]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[DPY19L1P2]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[NFIB]] | -0.50 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ZMYND11]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (15.2, -23.7); signed map (-24.9, 22.0). **Vector** length 79.6, 14.9% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.3 | +2.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.8 | +0.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology like domain family B member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,474,954-43,504,935 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40193 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

UniProt [Q6NSJ2](https://www.uniprot.org/uniprotkb/Q6NSJ2) carries no function annotation.

**Summary**, from NCBI Gene [653583](https://www.ncbi.nlm.nih.gov/gene/653583):

> Enables enzyme binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30499) · Entrez [653583](https://www.ncbi.nlm.nih.gov/gene/653583) · UniProt [Q6NSJ2](https://www.uniprot.org/uniprotkb/Q6NSJ2) · Ensembl [ENSG00000176531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176531)

## Data

Gene col 10726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10726); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10726]; `tensor/DDL_lfc|DDL_z.npy` [10726]; `embed/gene_vectors.npy` [10726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10726 or target_col == 10726). Every well: [[PHLDB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHLDB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
