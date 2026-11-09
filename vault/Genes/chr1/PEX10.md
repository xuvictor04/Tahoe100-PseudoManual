---
symbol: "PEX10"
type: "gene"
col: 8114
ensembl_id: "ENSG00000157911"
name: "peroxisomal biogenesis factor 10"
location: "1p36.32"
module: 1
arm: "+"
pooled_cpm: 7.48
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PEX10

*peroxisomal biogenesis factor 10* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.97× (z +11.5, q 5e-28, up in 17 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.29× (z +4.2, q 0.004, up in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.99×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.661× (z -6.7, q 9e-09, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRUB2]] (+0.60, fdr 1e-05), [[JMJD4]] (+0.60, fdr 1e-05), [[TRMT61A]] (+0.56, fdr 1e-05); moves opposite to [[MAGI3]] (-0.51, fdr 1e-05), [[LIN54]] (-0.44, fdr 4e-05), [[PRKCG]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8114.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.99×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +11.5 | 5e-28 | 17/19 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +10.7 | 3e-24 | 27/31 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.4 | 3e-11 | 12/14 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.004 | 16/47 (A-172, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.8 | 0.014 | 13/37 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.75×** | +3.3 | 0.079 | 7/35 (PANC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.3 | 0.079 | 13/36 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | 1.70× | +3.2 | 0.10 | 4/38 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 1.31× | +3.1 | 0.11 | 7/46 (NCI-H1573, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.661×** | -6.7 | 9e-09 | 25/43 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -5.9 | 9e-07 | 24/43 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.711×** | -5.5 | 5e-06 | 24/46 (Hs 766T, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -4.9 | 1e-04 | 18/45 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -4.8 | 2e-04 | 20/46 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.668×** | -4.6 | 3e-04 | 17/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.675×** | -4.5 | 5e-04 | 17/47 (HOP62, SW1417, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.668×** | -4.4 | 8e-04 | 18/45 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.695×** | -4.2 | 0.002 | 17/45 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.731×** | -3.6 | 0.017 | 16/47 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.737×** | -3.5 | 0.023 | 16/43 (RKO, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.751×** | -3.3 | 0.045 | 13/47 (RPMI-7951, RKO, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.739×** | -3.3 | 0.045 | 12/43 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.768×** | -3.0 | 0.095 | 3/47 (NCI-H1792, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 8.52 | 0 | 2 | — | [[IQ 1 (drug)]] 0.05 µM 0.0562× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0666× (z -12.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.140× (z -10.3) |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0628× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0407× (z -15.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 6.96 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0647× (z -9.2) |
| [[SW480 (line)]] | alt | 7.03 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRUB2]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[JMJD4]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 | STRING 447 |
| [[TRMT61A]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MCAT]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 | STRING 458 |
| [[DPH1]] | +0.55 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[NUBPL]] | +0.54 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[ZNF696]] | +0.54 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[MECR]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[COPS7A]] | +0.53 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[FAAP100]] | +0.53 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[RRN3]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DDX28]] | +0.51 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGI3]] | -0.51 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[LIN54]] | -0.44 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PRKCG]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[LINC01950]] | -0.44 | -0.28 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.3, 1.0); signed map (-4.5, -26.7). **Vector** length 45.6, 5.55% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.6 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.6 | -4.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:2,403,964-2,413,797 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF69 |
| Gene groups (HGNC) | Ring finger proteins; Peroxins; RING finger E3 ubiquitin protein ligases |
| Reactome | 4 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Peroxisomal protein import; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [O60683](https://www.uniprot.org/uniprotkb/O60683) (Peroxisome biogenesis factor 10):

> E3 ubiquitin-protein ligase component of a retrotranslocation channel required for peroxisome organization by mediating export of the PEX5 receptor from peroxisomes to the cytosol, thereby promoting PEX5 recycling. The retrotranslocation channel is composed of PEX2, PEX10 and PEX12; each subunit contributing transmembrane segments that coassemble into an open channel that specifically allows the passage of PEX5 through the peroxisomal membrane (By similarity). PEX10 also regulates PEX5 …

**Summary**, from NCBI Gene [5192](https://www.ncbi.nlm.nih.gov/gene/5192):

> This gene encodes a protein involved in import of peroxisomal matrix proteins. This protein localizes to the peroxisomal membrane. Mutations in this gene result in phenotypes within the Zellweger spectrum of peroxisomal biogenesis disorders, ranging from neonatal adrenoleukodystrophy to Zellweger syndrome. Alternative splicing results in two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8851) · Entrez [5192](https://www.ncbi.nlm.nih.gov/gene/5192) · UniProt [O60683](https://www.uniprot.org/uniprotkb/O60683) · Ensembl [ENSG00000157911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157911)

## Data

Gene col 8114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8114); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8114]; `tensor/DDL_lfc|DDL_z.npy` [8114]; `embed/gene_vectors.npy` [8114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8114 or target_col == 8114). Every well: [[PEX10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
