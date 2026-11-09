---
symbol: "UBL7"
type: "gene"
col: 6198
ensembl_id: "ENSG00000138629"
name: "ubiquitin like 7"
location: "15q24.1"
module: 74
arm: "+"
pooled_cpm: 7.81
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# UBL7

*ubiquitin like 7* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.89× (z +11.2, q 2e-26, up in 31 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.79× (z +10.8, q 7e-25, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.524× (z -6.8, q 4e-09, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRBN]] (+0.60, fdr 4e-05), [[MRPL10]] (+0.58, fdr 1e-05), [[PLEKHM3]] (+0.58, fdr 2e-04); moves opposite to [[ANKRD18A]] (-0.49, fdr 6e-04), [[TNPO2]] (-0.48, fdr 3e-04), [[ARGLU1]] (-0.46, fdr 0.001, ⚠ not reproduced), [[MRPS25]] (-0.45, fdr 1e-04).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.89×** | +11.2 | 2e-26 | 31/34 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +10.8 | 7e-25 | 46/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.59×** | +10.1 | 1e-21 | 42/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +8.8 | 2e-16 | 12/14 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.00×** | +7.3 | 3e-11 | 36/47 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.78×** | +5.4 | 7e-06 | 17/24 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.4 | 9e-04 | 18/35 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.51×** | +4.4 | 9e-04 | 18/38 (NCI-H23, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.031 | 6/36 (LoVo, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.061 | 14/47 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.2 | 0.062 | 3/48 (SK-MEL-2, SW48, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.075 | 12/42 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.096 | 5/44 (SW48, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -6.8 | 4e-09 | 34/47 (COLO 205, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.528×** | -6.7 | 4e-09 | 33/47 (A-427, KATO III, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.540×** | -6.5 | 2e-08 | 34/47 (SW48, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -5.1 | 6e-05 | 24/43 (HT-29, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.677×** | -4.1 | 0.004 | 16/47 (RKO, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.615×** | -3.7 | 0.024 | 11/48 (NCI-H2030, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.737× | -3.2 | 0.11 | 20/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.742× | -3.1 | 0.12 | 12/47 (Panc 03.27, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.48 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.20× (z +9.5) | — |
| [[A-172 (line)]] | wt | 7.08 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0526× (z -13.0) ⚠ toxic |
| [[A-427 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.159× (z -9.5) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 8.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 5.55 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0676× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 7.58 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0676× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 7.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRBN]] | +0.60 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[MRPL10]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PLEKHM3]] | +0.58 | +0.30 / +0.64 | both halves | 2e-04 |  |
| [[MRPL40]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ABTB1]] | +0.58 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[MARF1]] | +0.57 | +0.24 / +0.52 | both halves | 4e-04 |  |
| [[RETREG2]] | +0.57 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[THYN1]] | +0.57 | +0.48 / +0.36 | both halves | 1e-04 |  |
| [[SNAPIN]] | +0.56 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[BCKDK]] | +0.55 | +0.44 / +0.29 | both halves | 3e-04 |  |
| [[FRG1CP]] | +0.55 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[DHX40]] | +0.55 | +0.40 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18A]] | -0.49 | -0.22 / -0.29 | both halves | 6e-04 |  |
| [[TNPO2]] | -0.48 | -0.37 / -0.29 | both halves | 3e-04 |  |
| [[ARGLU1]] | -0.46 | -0.45 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[SNX5]] | -0.45 | -0.15 / -0.35 | ⚠ not reproduced | 0.001 |  |
| [[DUS2]] | -0.45 | -0.19 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[MRPS25]] | -0.45 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[DGUOK-AS1]] | -0.44 | -0.28 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.387). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.6, -46.8); signed map (-20.6, 8.5). **Vector** length 54.6, 8.19% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +10.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +2.4 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +8.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.2 | +2.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -6.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,445,977-74,461,182 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BMSC-UbP, MGC14421 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S82](https://www.uniprot.org/uniprotkb/Q96S82) (Ubiquitin-like protein 7):

> Interferon-stimulated protein that positively regulates RNA virus-triggered innate immune signaling. Mechanistically, promotes 'Lys-27'-linked polyubiquitination of MAVS through TRIM21 leading to enhanced the IFN signaling pathway.

**Summary**, from NCBI Gene [84993](https://www.ncbi.nlm.nih.gov/gene/84993):

> Enables protein-macromolecule adaptor activity. Involved in antiviral innate immune response. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28221) · Entrez [84993](https://www.ncbi.nlm.nih.gov/gene/84993) · UniProt [Q96S82](https://www.uniprot.org/uniprotkb/Q96S82) · Ensembl [ENSG00000138629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138629)

## Data

Gene col 6198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6198); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6198]; `tensor/DDL_lfc|DDL_z.npy` [6198]; `embed/gene_vectors.npy` [6198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6198 or target_col == 6198). Every well: [[UBL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
