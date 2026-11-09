---
symbol: "ETFBKMT"
type: "gene"
col: 6267
ensembl_id: "ENSG00000139160"
name: "electron transfer flavoprotein subunit beta lysine methyltransferase"
location: "12p11.21"
module: 21
arm: "+"
pooled_cpm: 2.05
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ETFBKMT

*electron transfer flavoprotein subunit beta lysine methyltransferase* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.10× (z +14.8, q 0e+00, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.92× (z +13.7, q 2e-40, up in 27 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.488× (z -6.5, q 4e-08, down in 20 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.669× (z -3.7, q 0.048, down in 14 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.0760×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASL-DT]] (+0.69, fdr 7e-06), [[NDUFV2-AS1]] (+0.66, fdr 7e-06), [[GEMIN7-AS1]] (+0.66, fdr 7e-06); moves opposite to [[NUP205]] (-0.53, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.10×** | +14.8 | 0e+00 | 6/8 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +13.7 | 2e-40 | 27/30 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.41×** | +12.9 | 6e-36 | 2/2 (HOP62, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.88×** | +11.4 | 1e-27 | 2/3 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +8.6 | 8e-16 | 26/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.37×** | +7.8 | 6e-13 | 23/41 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.0 | 1e-07 | 4/12 (NCI-H2347, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +5.9 | 3e-07 | 17/40 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.005 | 8/28 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.8 | 0.010 | 2/9 (PANC-1, A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.014 | 1/42 (A-427) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.6 | 0.018 | 7/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.50×** | +3.4 | 0.029 | 2/24 (LOX-IMVI, SW 900) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.058 | 1/38 (NCI-H460) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.065 | 4/38 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6267.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.0760×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.488×** | -6.5 | 4e-08 | 20/44 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.669×** | -3.7 | 0.048 | 14/37 (A498, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -3.7 | 0.048 | 12/39 (RPMI-7951, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.696× | -3.3 | 0.12 | 5/38 (Panc 03.27, NCI-H23, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.688× | -3.3 | 0.12 | 11/38 (AsPC-1, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0760× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASL-DT]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[NDUFV2-AS1]] | +0.66 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[GEMIN7-AS1]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.65 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[PPM1N]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[BTG1-DT]] | +0.64 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LINC02175]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CYP2U1-AS1]] | +0.64 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[CFL1P1-1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SLC13A4]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[NPW]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[CTDSPL2-DT]] | +0.62 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP205]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.5, 29.8); signed map (37.1, 4.3). **Vector** length 34.9, 3.34% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +14.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -6.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -3.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | electron transfer flavoprotein subunit beta lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:31,647,160-31,673,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp451L235, MGC50559; previously C12orf72, METTL20 |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 1 pathways, smallest: Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXQ9](https://www.uniprot.org/uniprotkb/Q8IXQ9) (Electron transfer flavoprotein beta subunit lysine methyltransferase):

> Protein-lysine methyltransferase that selectively trimethylates the flavoprotein ETFB in mitochondria. Thereby, may negatively regulate the function of ETFB in electron transfer from Acyl-CoA dehydrogenases to the main respiratory chain.

**Summary**, from NCBI Gene [254013](https://www.ncbi.nlm.nih.gov/gene/254013):

> Enables heat shock protein binding activity and protein-lysine N-methyltransferase activity. Involved in negative regulation of fatty acid beta-oxidation using acyl-CoA dehydrogenase. Located in mitochondrial matrix. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28739) · Entrez [254013](https://www.ncbi.nlm.nih.gov/gene/254013) · UniProt [Q8IXQ9](https://www.uniprot.org/uniprotkb/Q8IXQ9) · Ensembl [ENSG00000139160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139160)

## Data

Gene col 6267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6267); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6267]; `tensor/DDL_lfc|DDL_z.npy` [6267]; `embed/gene_vectors.npy` [6267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6267 or target_col == 6267). Every well: [[ETFBKMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETFBKMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
