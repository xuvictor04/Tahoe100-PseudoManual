---
symbol: "IDH3B"
type: "gene"
col: 2126
ensembl_id: "ENSG00000101365"
name: "isocitrate dehydrogenase (NAD(+)) 3 non-catalytic subunit beta"
location: "20p13"
module: 7
arm: "+"
pooled_cpm: 25.27
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# IDH3B

*isocitrate dehydrogenase (NAD(+)) 3 non-catalytic subunit beta* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +10.6, q 1e-23, up in 40 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.75× (z +5.2, q 2e-05, up in 35 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM42]] (+0.66, fdr 7e-06), [[STOML2]] (+0.63, fdr 7e-06), [[DOHH]] (+0.59, fdr 1e-05); moves opposite to [[CBX3]] (-0.49, fdr 2e-04), [[G3BP2]] (-0.46, fdr 1e-04), [[ENTPD4]] (-0.45, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.11×** | +10.6 | 1e-23 | 40/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +9.9 | 1e-20 | 29/34 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +5.6 | 3e-06 | 30/38 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +5.2 | 2e-05 | 35/48 (LoVo, HOP62, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.4 | 1e-03 | 28/48 (SNU-423, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.59×** | +4.3 | 0.001 | 29/47 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.62×** | +4.3 | 0.001 | 29/47 (HOP62, NCI-H460, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.58×** | +4.1 | 0.003 | 27/45 (A-427, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.52×** | +3.9 | 0.005 | 27/44 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.010 | 28/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.7 | 0.012 | 23/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.7 | 0.012 | 2/48 (C-33 A, CHP-212) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.46×** | +3.5 | 0.020 | 27/47 (SW480, SW48, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.024 | 21/47 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.98×** | +3.4 | 0.025 | 22/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.795× | -3.1 | 0.95 | 24/48 (CHP-212, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 34.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +11.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 23.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 31.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 25.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C-33 A (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.61× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM42]] | +0.66 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[STOML2]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 | STRING 419 |
| [[DOHH]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RNF7]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[PQBP1]] | +0.52 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[MTX3]] | +0.51 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[MRPL45]] | +0.51 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[WDR74]] | +0.50 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[NDUFS3]] | +0.50 | +0.56 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 634 |
| [[BECN1]] | +0.49 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[LAMTOR1]] | +0.49 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[GFER]] | +0.48 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX3]] | -0.49 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[G3BP2]] | -0.46 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[ENTPD4]] | -0.45 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ADGRE3]] | -0.43 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[ITGB1]] | -0.42 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[TMSB4X]] | -0.41 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[PTMS]] | -0.41 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[RELL1]] | -0.41 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.40 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[EXTL3]] | -0.40 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.309). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-51.1, 1.6); signed map (-4.3, -19.5). **Vector** length 48.8, 10.2% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.0 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Decitabine (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | isocitrate dehydrogenase (NAD(+)) 3 non-catalytic subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:2,658,395-2,664,219 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RP46 |
| Gene groups (HGNC) | Isocitrate dehydrogenases |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43837](https://www.uniprot.org/uniprotkb/O43837) (Isocitrate dehydrogenase):

> Plays a structural role to facilitate the assembly and ensure the full activity of the enzyme catalyzing the decarboxylation of isocitrate (ICT) into alpha-ketoglutarate. The heterodimer composed of the alpha (IDH3A) and beta (IDH3B) subunits and the heterodimer composed of the alpha (IDH3A) and gamma (IDH3G) subunits, have considerable basal activity but the full activity of the heterotetramer (containing two subunits of IDH3A, one of IDH3B and one of IDH3G) requires the assembly and …

**Summary**, from NCBI Gene [3420](https://www.ncbi.nlm.nih.gov/gene/3420):

> Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isocitrate dehydrogenases, one of which is mitochondrial and the other predominantly cytosolic. …

**Accessions** — [HGNC:5385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5385) · Entrez [3420](https://www.ncbi.nlm.nih.gov/gene/3420) · UniProt [O43837](https://www.uniprot.org/uniprotkb/O43837) · Ensembl [ENSG00000101365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101365)

## Data

Gene col 2126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2126); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2126]; `tensor/DDL_lfc|DDL_z.npy` [2126]; `embed/gene_vectors.npy` [2126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2126 or target_col == 2126). Every well: [[IDH3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDH3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
