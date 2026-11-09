---
symbol: "FRAT2"
type: "gene"
col: 11177
ensembl_id: "ENSG00000181274"
name: "FRAT regulator of Wnt signaling pathway 2"
location: "10q24.1"
module: 69
arm: "+"
pooled_cpm: 2.52
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# FRAT2

*FRAT regulator of Wnt signaling pathway 2* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.37× (z +8.9, q 3e-16, up in 21 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.359× (z -7.7, q 6e-12, down in 31 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.251× (z -5.5, q 1e-05, down in 20 of 31 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBALD1]] (+0.67, fdr 1e-05), [[UBALD2]] (+0.61, fdr 1e-04), [[KLHL24]] (+0.60, fdr 3e-05); moves opposite to [[PTPN11]] (-0.55, fdr 6e-05), [[XRCC5]] (-0.50, fdr 8e-05), [[EIF3I]] (-0.49, fdr 5e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +8.9 | 3e-16 | 21/31 (KATO III, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.84×** | +6.2 | 1e-07 | 15/29 (SW1417, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +6.0 | 3e-07 | 25/45 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +5.4 | 7e-06 | 21/42 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +5.1 | 3e-05 | 0/4 | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +5.1 | 3e-05 | 1/6 (AsPC-1) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +4.5 | 5e-04 | 15/44 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +4.2 | 0.002 | 10/29 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +3.8 | 0.010 | 8/45 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.99×** | +3.7 | 0.013 | 2/23 (LS 180, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +3.7 | 0.013 | 7/14 (A-427, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.3 | 0.047 | 6/16 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.047 | 2/44 (J82, Panc 03.27) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +3.2 | 0.058 | 2/16 (A498, NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.51×** | +3.1 | 0.075 | 4/22 (Hs 766T, LS 180, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.359×** | -7.7 | 6e-12 | 31/45 (A498, AsPC-1, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.251×** | -5.5 | 1e-05 | 20/31 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.370×** | -5.4 | 2e-05 | 22/45 (KATO III, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.365×** | -4.0 | 0.010 | 15/25 (SW1417, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.581×** | -3.9 | 0.012 | 15/37 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.404×** | -3.6 | 0.032 | 11/25 (HT-29, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -3.4 | 0.049 | 13/36 (HT-29, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.424×** | -3.4 | 0.049 | 6/23 (HEC-1-A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.639×** | -3.2 | 0.086 | 11/44 (SW48, A498, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 5 µM |  | 0.747× | -3.1 | 0.12 | 5/44 (PANC-1, Hs 766T, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 5.70 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0650× (z -10.2) |
| [[A-172 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 16 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBALD1]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[UBALD2]] | +0.61 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[KLHL24]] | +0.60 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[SPSB3]] | +0.59 | +0.31 / +0.72 | both halves | 2e-04 |  |
| [[WDR48]] | +0.58 | +0.28 / +0.61 | both halves | 3e-04 |  |
| [[COQ8A]] | +0.55 | +0.40 / +0.63 | both halves | 4e-05 |  |
| [[ARRDC2]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[IRS2]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[GARRE1]] | +0.55 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[HDAC5]] | +0.55 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[MNT]] | +0.55 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[JMY]] | +0.54 | +0.20 / +0.64 | both halves | 7e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN11]] | -0.55 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[XRCC5]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[EIF3I]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CLTC]] | -0.48 | -0.45 / -0.52 | both halves | 3e-05 | pathway: Signaling by WNT |
| [[GTF2H3]] | -0.47 | -0.16 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[PDAP1]] | -0.46 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[UBE2V1]] | -0.46 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[NUP205]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[FAM91A1]] | -0.46 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[PTGES3]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[OPA1]] | -0.45 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GSS]] | -0.45 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[PSMD14]] | -0.44 | -0.47 / -0.39 | both halves | 5e-05 | pathway: Degradation of beta-catenin by the destruction complex |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.558). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.8, -45.0); signed map (-15.3, 9.0). **Vector** length 50.1, 6.68% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +8.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -7.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.9 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | FRAT regulator of Wnt signaling pathway 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:97,332,497-97,334,729 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 5 pathways, smallest: Beta-catenin phosphorylation cascade; Disassembly of the destruction complex and recruitment of AXIN to the membrane; Degradation of beta-catenin by the destruction complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O75474](https://www.uniprot.org/uniprotkb/O75474) (GSK-3-binding protein FRAT2):

> Positively regulates the Wnt signaling pathway by stabilizing beta-catenin through the association with GSK-3.

**Summary**, from NCBI Gene [23401](https://www.ncbi.nlm.nih.gov/gene/23401):

> The protein encoded by this intronless gene belongs to the GSK-3-binding protein family. Studies show that this protein plays a role as a positive regulator of the WNT signaling pathway. It may be upregulated in tumor progression. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16048) · Entrez [23401](https://www.ncbi.nlm.nih.gov/gene/23401) · UniProt [O75474](https://www.uniprot.org/uniprotkb/O75474) · Ensembl [ENSG00000181274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181274)

## Data

Gene col 11177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11177); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11177]; `tensor/DDL_lfc|DDL_z.npy` [11177]; `embed/gene_vectors.npy` [11177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11177 or target_col == 11177). Every well: [[FRAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
