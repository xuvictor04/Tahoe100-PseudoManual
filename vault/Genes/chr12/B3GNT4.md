---
symbol: "B3GNT4"
type: "gene"
col: 10706
ensembl_id: "ENSG00000176383"
name: "UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 4"
location: "12q24.31"
module: 103
arm: "+"
pooled_cpm: 2.45
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# B3GNT4

*UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 4* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.13× (z +6.5, q 4e-08, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.01× (z +4.5, q 0.001, up in 3 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.382× (z -8.6, q 5e-15, down in 26 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISM2]] (+0.56, fdr 1e-05), [[UPK1A-AS1]] (+0.53, fdr 1e-04), [[GYS1]] (+0.52, fdr 4e-05); moves opposite to [[CFAP298]] (-0.45, fdr 6e-05), [[ATR]] (-0.44, fdr 1e-04), [[MTOR]] (-0.44, fdr 9e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +6.5 | 4e-08 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +6.0 | 7e-07 | 1/11 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.01×** | +4.5 | 0.001 | 3/14 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.2 | 0.004 | 2/16 (NCI-H2347, SW48) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.004 | 8/24 (NCI-H460, BT-474, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.1 | 0.004 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +3.7 | 0.019 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.62× | +3.1 | 0.13 | 5/25 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.17 | 4/35 (C-33 A, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.382×** | -8.6 | 5e-15 | 26/39 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -6.7 | 6e-09 | 23/44 (NCI-H23, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -5.5 | 6e-06 | 17/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.552×** | -5.3 | 1e-05 | 12/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -5.3 | 1e-05 | 15/37 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.594×** | -4.6 | 3e-04 | 13/39 (A-427, NCI-H460, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -4.6 | 4e-04 | 14/24 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.622×** | -4.2 | 0.002 | 10/34 (NCI-H23, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.650×** | -3.7 | 0.015 | 11/18 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Naproxen (drug)]] 0.5 µM |  | **0.664×** | -3.6 | 0.015 | 6/44 (A498, HT-29, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.509×** | -3.2 | 0.084 | 8/33 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 8.56 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0871× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 3.14 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0731× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.78 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0848× (z -9.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 2.39 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0638× (z -11.5) |
| [[A-172 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.918 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.896 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISM2]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[UPK1A-AS1]] | +0.53 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[GYS1]] | +0.52 | +0.41 / +0.62 | both halves | 4e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[ZNF395]] | +0.51 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[LINC00482]] | +0.51 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[ACADS]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[RYBP]] | +0.50 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[SMAD9]] | +0.50 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CASKIN1]] | +0.49 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[THAP8]] | +0.49 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[CAMSAP3]] | +0.48 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[EHD2]] | +0.47 | +0.32 / +0.45 | both halves | 2e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP298]] | -0.45 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[ATR]] | -0.44 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[MTOR]] | -0.44 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[TRNT1]] | -0.43 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[APPL2]] | -0.42 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ATE1]] | -0.42 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[PKP4]] | -0.42 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[POLR3E]] | -0.41 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[AAGAB]] | -0.40 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ARIH2]] | -0.40 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[UGGT2]] | -0.40 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[MTFR1]] | -0.40 | -0.47 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.5, -13.5); signed map (-29.5, 33.0). **Vector** length 41.1, 4.48% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +4.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.2 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +0.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -8.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.5 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.5 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -4.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,203,681-122,208,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B3GN-T4, beta3Gn-T4 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 6 pathways, smallest: Keratan sulfate biosynthesis; Keratan sulfate/keratin metabolism; O-linked glycosylation of mucins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0J1](https://www.uniprot.org/uniprotkb/Q9C0J1) (N-acetyllactosaminide beta-1,3-N-acetylglucosaminyltransferase 4):

> Beta-1,3-N-acetylglucosaminyltransferase involved in the synthesis of poly-N-acetyllactosamine. Has activity for type 2 oligosaccharides.

**Summary**, from NCBI Gene [79369](https://www.ncbi.nlm.nih.gov/gene/79369):

> This gene encodes a member of the beta-1,3-N-acetylglucosaminyltransferase protein family. The encoded enzyme is involved in the biosynthesis of poly-N-acetyllactosamine chains and prefers lacto-N-neotetraose as a substrate. It is a type II transmembrane protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15683) · Entrez [79369](https://www.ncbi.nlm.nih.gov/gene/79369) · UniProt [Q9C0J1](https://www.uniprot.org/uniprotkb/Q9C0J1) · Ensembl [ENSG00000176383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176383)

## Data

Gene col 10706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10706); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10706]; `tensor/DDL_lfc|DDL_z.npy` [10706]; `embed/gene_vectors.npy` [10706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10706 or target_col == 10706). Every well: [[B3GNT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GNT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
