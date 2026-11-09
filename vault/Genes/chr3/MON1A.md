---
symbol: "MON1A"
type: "gene"
col: 8857
ensembl_id: "ENSG00000164077"
name: "MON1 vesicular trafficking associated A"
location: "3p21.31"
module: 33
arm: "+"
pooled_cpm: 3.41
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MON1A

*MON1 vesicular trafficking associated A* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.27× (z +9.3, q 1e-17, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.632× (z -5.2, q 9e-05, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC10]] (+0.69, fdr 7e-06), [[ZNF496]] (+0.66, fdr 1e-05), [[CHCHD6]] (+0.66, fdr 1e-05); moves opposite to [[IFNAR1]] (-0.58, fdr 3e-05), [[SGO1-AS1]] (-0.56, fdr 4e-05), [[STAG2]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +9.3 | 1e-17 | 27/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.22×** | +9.0 | 4e-17 | 24/44 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +8.9 | 1e-16 | 12/20 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.85×** | +6.9 | 6e-10 | 20/45 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +6.7 | 2e-09 | 15/35 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +5.9 | 3e-07 | 17/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.71×** | +5.9 | 4e-07 | 1/4 (NCI-H2347) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +4.9 | 6e-05 | 14/36 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.6 | 3e-04 | 5/46 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.5 | 4e-04 | 3/11 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 8e-04 | 7/40 (KATO III, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +3.9 | 0.004 | 6/46 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.011 | 6/44 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.38×** | +3.6 | 0.013 | 2/17 (A498, NCI-H2347) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.35×** | +3.4 | 0.025 | 3/45 (LoVo, C32, …) | rises with dose |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.053 | 6/37 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.080 | 4/40 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.084 | 6/44 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.084 | 5/32 (NCI-H2030, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -5.2 | 9e-05 | 16/46 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -4.0 | 0.017 | 15/45 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -3.8 | 0.029 | 14/32 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.035 | 11/43 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 3.65 | 0 | 1 | — | [[Vortioxetine (drug)]] 0.05 µM 0.0561× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 4.36 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.254× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 4.15 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0742× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 3.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 6.99 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0664× (z -10.5) |
| [[A-172 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC10]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZNF496]] | +0.66 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[POLR3B]] | +0.65 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[MRPS23]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PEMT]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[HMOX2]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MPP3]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[POLR1B]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[RRP7BP]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PDCD11]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[WDR3]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNAR1]] | -0.58 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[STAG2]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PCM1]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[RO60]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.8, -30.2); signed map (-14.2, -52.9). **Vector** length 49.9, 5.79% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.7 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.4 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +1.8 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +0.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.2 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -0.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.0 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -0.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | MON1 vesicular trafficking associated A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,907,160-49,930,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13272, SAND1 |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VX9](https://www.uniprot.org/uniprotkb/Q86VX9) (Vacuolar fusion protein MON1 homolog A):

> Plays an important role in membrane trafficking through the secretory apparatus. Not involved in endocytic trafficking to lysosomes (By similarity). Acts in concert with CCZ1, as a guanine exchange factor (GEF) for RAB7, promotes the exchange of GDP to GTP, converting it from an inactive GDP-bound form into an active GTP-bound form.

**Summary**, from NCBI Gene [84315](https://www.ncbi.nlm.nih.gov/gene/84315):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in protein secretion. Predicted to act upstream of or within intracellular iron ion homeostasis and protein transport. Part of Mon1-Ccz1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28207) · Entrez [84315](https://www.ncbi.nlm.nih.gov/gene/84315) · UniProt [Q86VX9](https://www.uniprot.org/uniprotkb/Q86VX9) · Ensembl [ENSG00000164077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164077)

## Data

Gene col 8857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8857); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8857]; `tensor/DDL_lfc|DDL_z.npy` [8857]; `embed/gene_vectors.npy` [8857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8857 or target_col == 8857). Every well: [[MON1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MON1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
