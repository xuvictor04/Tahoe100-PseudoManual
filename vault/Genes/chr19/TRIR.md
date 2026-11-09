---
symbol: "TRIR"
type: "gene"
col: 4408
ensembl_id: "ENSG00000123144"
name: "telomerase RNA component interacting RNase"
location: "19p13.13"
module: 11
arm: "+"
pooled_cpm: 43.15
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# TRIR

*telomerase RNA component interacting RNase* — 19p13.13

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.04× (z +7.8, q 4e-12, up in 42 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 2.93×, Hs 766T 4.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A549 3.83×, NCI-H460 3.47×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.197×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H661 0.0780×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPA0]] (+0.66, fdr 7e-06), [[CHMP1A]] (+0.65, fdr 7e-06), [[KMT2B]] (+0.59, fdr 9e-06); moves opposite to [[SCOC]] (-0.57, fdr 3e-05), [[PGM2]] (-0.54, fdr 1e-05), [[MRPL30]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4408.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 2.93×, Hs 766T 4.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A549 3.83×, NCI-H460 3.47×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.04×** | +7.8 | 4e-12 | 42/46 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.86×** | +6.5 | 2e-08 | 33/40 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.66×** | +5.5 | 5e-06 | 41/47 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.60×** | +4.7 | 3e-04 | 30/44 (HepG2/C3A, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.4 | 0.001 | 34/47 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.49×** | +4.4 | 0.001 | 36/46 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.49×** | +4.2 | 0.002 | 28/47 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.39×** | +3.6 | 0.021 | 26/48 (SW480, LS 180, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.33× | +3.1 | 0.10 | 22/48 (C32, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.35× | +3.1 | 0.10 | 22/48 (SW 900, A498, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4408.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.197×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H661 0.0780×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.741× | -3.0 | 0.69 | 23/48 (HEC-1-A, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Hs 766T (line)]] | wt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H661 (line)]] | alt | 47.6 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0780× (z -9.2) |
| [[PANC-1 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 60.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA0]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CHMP1A]] | +0.65 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[KMT2B]] | +0.59 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[MEX3D]] | +0.56 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ZNF358]] | +0.55 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[GUSBP11]] | +0.55 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[SMG6]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TBC1D10B]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[GPATCH8]] | +0.54 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[GPATCH3]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[GATD1-DT]] | +0.51 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[EGLN2]] | +0.50 | +0.39 / +0.61 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCOC]] | -0.57 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PGM2]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MRPL30]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CFAP97]] | -0.53 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[UCHL5]] | -0.51 | -0.49 / -0.43 | both halves | 4e-05 |  |
| [[UBA5]] | -0.50 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[GTF3A]] ⚠ | -0.49 | -0.48 / -0.36 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[DNAJC10]] | -0.48 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[TSNAX]] | -0.48 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[ACP1]] | -0.47 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PAICS]] | -0.47 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[SELENOF]] | -0.46 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[DDHD2]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.156). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-27.9, -12.4); signed map (-18.4, 2.3). **Vector** length 56.7, 13.5% of its response variance represented; |z| ≥ 3 in 448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +3.0 | +5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.9 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.5 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | -0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | telomerase RNA component interacting RNase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,730,640-12,734,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2803, fSAP18, TERCIR; previously C19orf43 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ61](https://www.uniprot.org/uniprotkb/Q9BQ61) (Protein TRIR):

> RNA-binding protein involved in the resolution of sister telomere cohesion during mitosis. Binds telomeric repeat-containing RNA (TERRA) and limits the accumulation of TERRA RNA-DNA hybrids (R-loops) at telomeres, thereby contributing to sister telomere cohesion resolution. Acts as a negative regulator of protein phosphatase 4 (PP4) during the DNA damage response. Inhibits PP4-mediated dephosphorylation by interfering with the association of the catalytic subunit PPP4C with the regulatory …

**Summary**, from NCBI Gene [79002](https://www.ncbi.nlm.nih.gov/gene/79002):

> Enables 3'-5' exonuclease activity and 5'-3' exonuclease activity. Involved in rRNA catabolic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28424) · Entrez [79002](https://www.ncbi.nlm.nih.gov/gene/79002) · UniProt [Q9BQ61](https://www.uniprot.org/uniprotkb/Q9BQ61) · Ensembl [ENSG00000123144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123144)

## Data

Gene col 4408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4408); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4408]; `tensor/DDL_lfc|DDL_z.npy` [4408]; `embed/gene_vectors.npy` [4408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4408 or target_col == 4408). Every well: [[TRIR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
