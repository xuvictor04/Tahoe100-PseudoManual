---
symbol: "ZSWIM1"
type: "gene"
col: 9675
ensembl_id: "ENSG00000168612"
name: "zinc finger SWIM-type containing 1"
location: "20q13.12"
module: 7
arm: "+"
pooled_cpm: 6.32
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZSWIM1

*zinc finger SWIM-type containing 1* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.86× (z +6.6, q 2e-08, up in 24 of 35 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.80× (z +6.5, q 2e-08, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.638× (z -5.0, q 4e-04, down in 19 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.679× (z -4.3, q 0.005, down in 19 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF687]] (+0.70, fdr 7e-06), [[MRPS18A]] (+0.70, fdr 7e-06), [[MED7]] (+0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +6.6 | 2e-08 | 24/35 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +6.5 | 2e-08 | 25/46 (A498, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +6.0 | 5e-07 | 28/45 (NCI-H23, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +5.6 | 3e-06 | 24/47 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.7 | 3e-04 | 15/47 (CFPAC-1, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 6e-04 | 15/44 (LOX-IMVI, LS 180, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +4.5 | 6e-04 | 18/43 (NCI-H2030, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 15/40 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.3 | 0.001 | 11/34 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.002 | 15/47 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.002 | 13/39 (RKO, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.027 | 7/47 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -5.0 | 4e-04 | 19/42 (NCI-H460, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -4.3 | 0.005 | 19/46 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.681×** | -4.1 | 0.008 | 15/36 (COLO 205, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.692×** | -3.9 | 0.012 | 12/44 (Panc 03.27, RPMI-7951, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.724×** | -3.6 | 0.039 | 19/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.745× | -3.3 | 0.10 | 12/43 (LS 180, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.750× | -3.2 | 0.10 | 12/42 (HS-578T, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.752× | -3.2 | 0.10 | 18/29 (CFPAC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.753× | -3.1 | 0.10 | 7/47 (NCI-H661, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.760× | -3.0 | 0.12 | 10/46 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Sunitinib (drug)]] 0.5 µM |  | 0.760× | -3.0 | 0.12 | 11/44 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.67 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0866× (z -10.5) |
| [[C-33 A (line)]] | alt | 9.10 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0725× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 5.57 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 6.37 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0732× (z -12.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0825× (z -11.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 8.11 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 5.05 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.05 µM 0.0751× (z -8.5) |
| [[A-427 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF687]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[MRPS18A]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MED7]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZNF574]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ZNF134]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[DPF2]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[KAT5]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.66 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[SMG8]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ZNF646]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.65 | +0.63 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.4, 10.0); signed map (-0.4, -25.9). **Vector** length 58.9, 8.14% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | -0.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.6 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.2 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.6 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Acetohexamide (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger SWIM-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,881,227-45,885,266 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ337O18.5; previously C20orf162 |
| Gene groups (HGNC) | Zinc fingers SWIM-type |
| Matched by | ensembl_id |

UniProt [Q9BR11](https://www.uniprot.org/uniprotkb/Q9BR11) carries no function annotation.

**Summary**, from NCBI Gene [90204](https://www.ncbi.nlm.nih.gov/gene/90204):

> Predicted to enable zinc ion binding activity. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16155) · Entrez [90204](https://www.ncbi.nlm.nih.gov/gene/90204) · UniProt [Q9BR11](https://www.uniprot.org/uniprotkb/Q9BR11) · Ensembl [ENSG00000168612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168612)

## Data

Gene col 9675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9675); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9675]; `tensor/DDL_lfc|DDL_z.npy` [9675]; `embed/gene_vectors.npy` [9675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9675 or target_col == 9675). Every well: [[ZSWIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSWIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
