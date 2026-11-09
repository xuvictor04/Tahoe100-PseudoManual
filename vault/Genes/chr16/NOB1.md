---
symbol: "NOB1"
type: "gene"
col: 6490
ensembl_id: "ENSG00000141101"
name: "NIN1 (RPN12) binding protein 1 homolog"
location: "16q22.1"
module: 33
arm: "+"
pooled_cpm: 39.85
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NOB1

*NIN1 (RPN12) binding protein 1 homolog* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.52× (z +4.9, q 5e-04, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.772× (z -4.3, q 0.010, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.242×, NCI-H2030 0.443×, NCI-H460 0.419×, RKO 0.470×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (RKO 0.326×, MIA PaCa-2 0.327×, LS 180 0.436×, SNU-1 0.404×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.312×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS2]] (+0.71, fdr 7e-06), [[RPP40]] (+0.69, fdr 9e-06), [[YDJC]] (+0.68, fdr 7e-06); moves opposite to [[PRKACA]] (-0.50, fdr 3e-05), [[SKA2]] (-0.49, fdr 5e-05), [[MYL6]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +4.9 | 5e-04 | 28/48 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.7 | 5e-04 | 33/43 (NCI-H2347, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.13×** | +4.6 | 5e-04 | 34/48 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.48×** | +4.6 | 5e-04 | 34/46 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +3.9 | 0.009 | 26/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.39×** | +3.9 | 0.009 | 24/48 (CFPAC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.8 | 0.014 | 0/48 | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.096 | 21/47 (HEC-1-A, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.097 | 26/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.11 | 19/48 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.31× | +3.0 | 0.13 | 21/46 (HT-29, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6490.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.242×, NCI-H2030 0.443×, NCI-H460 0.419×, RKO 0.470×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (RKO 0.326×, MIA PaCa-2 0.327×, LS 180 0.436×, SNU-1 0.404×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.312×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -4.3 | 0.010 | 24/48 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.066 | 25/47 (hTERT-HPNE, NCI-H2030, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.756× | -3.0 | 0.49 | 17/48 (J82, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 73.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -12.6) |
| [[RKO (line)]] | wt | 63.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -12.8) |
| [[SNU-1 (line)]] | wt | 63.2 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.312× (z -11.5) |
| [[LS 180 (line)]] | wt | 48.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 86.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 78.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS2]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | STRING 592 |
| [[RPP40]] | +0.69 | +0.69 / +0.57 | both halves | 9e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 811 |
| [[YDJC]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[IMP4]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 866 |
| [[NOA1]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 | STRING 533 |
| [[ZNF74]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[NLE1]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 | STRING 722 |
| [[RSL1D1]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 | STRING 721 |
| [[NKRF]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[EIF4A2]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[FOXO3B]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SLX9]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 | same gene group; STRING 920 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKACA]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SKA2]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[MYL6]] | -0.49 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[EIF4EBP2]] | -0.48 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.1, -7.8); signed map (-16.5, -24.3). **Vector** length 99.8, 27.7% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | NIN1 (RPN12) binding protein 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,741,871-69,754,926 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOB1P, ART-4, MST158; previously PSMD8BP1 |
| Gene groups (HGNC) | Endoribonucleases; Ribosome biogenesis factors |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULX3](https://www.uniprot.org/uniprotkb/Q9ULX3) (RNA-binding protein NOB1):

> May play a role in mRNA degradation (Probable). Endonuclease required for processing of 20S pre-rRNA precursor and biogenesis of 40S ribosomal subunits (By similarity).

**Summary**, from NCBI Gene [28987](https://www.ncbi.nlm.nih.gov/gene/28987):

> In yeast, over 200 protein and RNA cofactors are required for ribosome assembly, and these are generally conserved in eukaryotes. These factors orchestrate modification and cleavage of the initial 35S precursor rRNA transcript into the mature 18S, 5.8S, and 25S rRNAs, folding of the rRNA, and binding of ribosomal proteins and 5S RNA. Nob1 is involved in pre-rRNA processing. In a late cytoplasmic processing step, Nob1 cleaves a 20S rRNA intermediate at cleavage site D to produce the mature 18S …

**Accessions** — [HGNC:29540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29540) · Entrez [28987](https://www.ncbi.nlm.nih.gov/gene/28987) · UniProt [Q9ULX3](https://www.uniprot.org/uniprotkb/Q9ULX3) · Ensembl [ENSG00000141101](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141101)

## Data

Gene col 6490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6490); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6490]; `tensor/DDL_lfc|DDL_z.npy` [6490]; `embed/gene_vectors.npy` [6490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6490 or target_col == 6490). Every well: [[NOB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
