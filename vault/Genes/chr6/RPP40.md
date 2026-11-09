---
symbol: "RPP40"
type: "gene"
col: 4572
ensembl_id: "ENSG00000124787"
name: "ribonuclease P/MRP subunit p40"
location: "6p25.1"
module: 33
arm: "+"
pooled_cpm: 3.54
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RPP40

*ribonuclease P/MRP subunit p40* — 6p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.05× (z +9.1, q 7e-17, up in 2 of 6 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.93× (z +5.4, q 8e-06, up in 16 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.434× (z -7.0, q 1e-09, down in 25 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.253×); [[Digitoxin (drug)]] 0.05 µM in 1 line (HS-578T 0.0642×); [[Fenofibrate (drug)]] 5 µM in 1 line (LOX-IMVI 0.0658×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOB1]] (+0.69, fdr 9e-06), [[MRPS26]] (+0.69, fdr 1e-05), [[NLE1]] (+0.67, fdr 1e-05); moves opposite to [[GNAS]] (-0.57, fdr 3e-05), [[CD63]] (-0.53, fdr 6e-05), [[C2]] (-0.52, fdr 4e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.05×** | +9.1 | 7e-17 | 2/6 (A498, PANC-1) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.75×** | +8.5 | 4e-15 | 13/16 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +7.4 | 4e-11 | 3/7 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +6.6 | 6e-09 | 17/27 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +6.1 | 1e-07 | 12/20 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.93×** | +5.4 | 8e-06 | 16/39 (PANC-1, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +5.3 | 9e-06 | 18/43 (NCI-H2030, LS 180, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.86×** | +5.2 | 1e-05 | 20/44 (HOP62, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.75×** | +4.7 | 1e-04 | 19/45 (LoVo, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +4.6 | 2e-04 | 17/43 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.78×** | +4.5 | 3e-04 | 3/10 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +4.0 | 0.003 | 16/43 (J82, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +3.9 | 0.003 | 15/42 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.004 | 11/42 (HOP62, BT-474, …) | rises with dose | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **2.41×** | +3.9 | 0.004 | 6/19 (PANC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.021 | 9/39 (Hs 766T, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.036 | 11/34 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.037 | 4/44 (NCI-H2030, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4572.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.253×); [[Digitoxin (drug)]] 0.05 µM in 1 line (HS-578T 0.0642×); [[Fenofibrate (drug)]] 5 µM in 1 line (LOX-IMVI 0.0658×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.434×** | -7.0 | 1e-09 | 25/44 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -4.4 | 0.004 | 15/42 (KATO III, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.755× | -3.3 | 0.13 | 17/35 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.674× | -3.3 | 0.13 | 13/41 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.43 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0642× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 3.23 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0658× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 7.86 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -9.5) |
| [[A-172 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOB1]] | +0.69 | +0.69 / +0.57 | both halves | 9e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 811 |
| [[MRPS26]] | +0.69 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[NLE1]] | +0.67 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.66 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[DCTPP1]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MRPS23]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ALKBH2]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[NEIL2]] | +0.62 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[TMEM177]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[NPM3]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[EMSLR]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.57 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CD63]] | -0.53 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[C2]] | -0.52 | -0.47 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-45.1, -8.3); signed map (-16.5, -24.8). **Vector** length 57.3, 8.89% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.5 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -4.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.0 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.5 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease P/MRP subunit p40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.1 — chr6:4,994,717-5,004,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA428J1.3; previously RNASEP1 |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Reactome | 6 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O75818](https://www.uniprot.org/uniprotkb/O75818) (Ribonuclease P protein subunit p40):

> Component of ribonuclease P, a ribonucleoprotein complex that generates mature tRNA molecules by cleaving their 5'-ends. Also a component of the MRP ribonuclease complex, which cleaves pre-rRNA sequences.

**Summary**, from NCBI Gene [10799](https://www.ncbi.nlm.nih.gov/gene/10799):

> Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Part of multimeric ribonuclease P complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20992) · Entrez [10799](https://www.ncbi.nlm.nih.gov/gene/10799) · UniProt [O75818](https://www.uniprot.org/uniprotkb/O75818) · Ensembl [ENSG00000124787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124787)

## Data

Gene col 4572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4572); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4572]; `tensor/DDL_lfc|DDL_z.npy` [4572]; `embed/gene_vectors.npy` [4572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4572 or target_col == 4572). Every well: [[RPP40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPP40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
