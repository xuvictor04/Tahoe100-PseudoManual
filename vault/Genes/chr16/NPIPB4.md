---
symbol: "NPIPB4"
type: "gene"
col: 11743
ensembl_id: "ENSG00000185864"
name: "nuclear pore complex interacting protein family member B4"
location: "16p12.2"
module: 65
arm: "-"
pooled_cpm: 10.5
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# NPIPB4

*nuclear pore complex interacting protein family member B4* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +8.7, q 2e-15, up in 26 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.528× (z -6.9, q 3e-09, down in 21 of 37 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (J82 0.0407×, NCI-H460 0.165×, HT-29 0.229×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (C-33 A 0.107×); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (SW 900 0.0589×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AsPC-1 0.0794×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPIPB5]] (+0.89, fdr 7e-06), [[NUTM2B-AS1]] (+0.66, fdr 1e-05), [[RNF32-AS1]] (+0.62, fdr 1e-05); moves opposite to [[WRAP53]] (-0.65, fdr 1e-05), [[DUSP11]] (-0.64, fdr 1e-05), [[PRMT9]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +8.7 | 2e-15 | 26/43 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.1 | 0.014 | 11/46 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.027 | 11/46 (COLO 205, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.7 | 0.027 | 10/38 (C32, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.38×** | +3.4 | 0.066 | 5/44 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.12 | 10/45 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.36× | +3.2 | 0.12 | 5/43 (C-33 A, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.14 | 5/45 (J82, HOP62, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | 1.21× | +3.1 | 0.14 | 5/47 (RKO, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11743.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (J82 0.0407×, NCI-H460 0.165×, HT-29 0.229×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (C-33 A 0.107×); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (SW 900 0.0589×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AsPC-1 0.0794×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.528×** | -6.9 | 3e-09 | 21/37 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.675× | -3.2 | 0.38 | 8/42 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | 0.760× | -3.1 | 0.38 | 17/36 (COLO 205, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 9.22 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0794× (z -9.5) |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.107× (z -10.2) |
| [[HT-29 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -8.6) ⚠ toxic |
| [[J82 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0407× (z -17.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.147× (z -9.3) |
| [[LS 180 (line)]] | wt | 7.52 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0895× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 8.45 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0994× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.107× (z -8.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -10.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 9.20 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0721× (z -8.7) |
| [[SW 900 (line)]] | alt | 5.48 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0589× (z -9.7) |
| [[A-172 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB5]] | +0.89 | +0.84 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[NUTM2B-AS1]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[PIEZO1]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.61 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ANKLE2]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PEPD]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SEMA6A-AS1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CDV3]] | +0.57 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[NUTM2A-AS1]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[FER]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CLIP1]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP53]] | -0.65 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[DUSP11]] | -0.64 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[PRMT9]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CNOT8]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[SNAPC3]] | -0.63 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[FAM168A]] | -0.63 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[ZNF230]] | -0.62 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ARL6]] | -0.62 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[FAM104A]] | -0.61 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[EID2B]] | -0.61 | -0.40 / -0.60 | both halves | 4e-05 |  |
| [[MED23]] | -0.61 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.61 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (6.8, -12.1); signed map (10.1, -7.4). **Vector** length 50.3, 6.06% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | +1.9 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +1.7 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.7 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.0 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | -6.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | nuclear pore complex interacting protein family member B4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:21,834,582-21,880,827 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [C9JG80](https://www.uniprot.org/uniprotkb/C9JG80) carries no function annotation.

**Summary**, from NCBI Gene [440345](https://www.ncbi.nlm.nih.gov/gene/440345):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:41985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41985) · Entrez [440345](https://www.ncbi.nlm.nih.gov/gene/440345) · UniProt [C9JG80](https://www.uniprot.org/uniprotkb/C9JG80) · Ensembl [ENSG00000185864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185864)

## Data

Gene col 11743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11743); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11743]; `tensor/DDL_lfc|DDL_z.npy` [11743]; `embed/gene_vectors.npy` [11743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11743 or target_col == 11743). Every well: [[NPIPB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPIPB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
