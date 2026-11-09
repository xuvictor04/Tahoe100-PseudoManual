---
symbol: "ABCF3"
type: "gene"
col: 8421
ensembl_id: "ENSG00000161204"
name: "ATP binding cassette subfamily F member 3"
location: "3q27.1"
module: 127
arm: "+"
pooled_cpm: 14.92
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# ABCF3

*ATP binding cassette subfamily F member 3* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.06× (z +10.2, q 2e-21, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.666× (z -5.7, q 5e-06, down in 30 of 48 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.768× (z -5.3, q 3e-05, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAP1]] (+0.74, fdr 7e-06), [[COASY]] (+0.73, fdr 7e-06), [[HARS2]] (+0.71, fdr 7e-06); moves opposite to [[FAM81A]] (-0.55, fdr 2e-05), [[IGF2BP3]] (-0.53, fdr 3e-05), [[AP1S2]] (-0.51, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +10.2 | 2e-21 | 43/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +8.6 | 2e-15 | 38/48 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.17×** | +8.5 | 4e-15 | 41/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +7.8 | 6e-13 | 34/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +7.3 | 2e-11 | 26/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +7.0 | 2e-10 | 11/48 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +6.9 | 3e-10 | 28/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +6.1 | 6e-08 | 28/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +6.0 | 1e-07 | 31/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +5.7 | 7e-07 | 29/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.1 | 2e-05 | 23/47 (LoVo, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.4 | 6e-04 | 14/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.1 | 0.002 | 16/47 (Hs 766T, SW1417, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 8/47 (hTERT-HPNE, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.004 | 15/48 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.050 | 16/46 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.666×** | -5.7 | 5e-06 | 30/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -5.3 | 3e-05 | 25/46 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -5.1 | 8e-05 | 17/28 (SW 900, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.704×** | -4.7 | 4e-04 | 19/40 (A-427, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.719×** | -4.3 | 0.002 | 15/34 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.758×** | -3.9 | 0.008 | 16/47 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.028 | 12/48 (HepG2/C3A, NCI-H2347, …) | rises with dose | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.790×** | -3.3 | 0.059 | 15/48 (SW480, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -3.2 | 0.097 | 16/48 (NCI-H23, LoVo, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.3 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.227× (z -8.5) |
| [[A-427 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAP1]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[COASY]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 | STRING 477 |
| [[HARS2]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 | STRING 660 |
| [[PRPF31]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[SRP68]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[DMAP1]] | +0.67 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[UCK1]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[RNF40]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[DNAJC14]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ZSCAN22]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[AARS2]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[IGF2BP3]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[AP1S2]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.3, -2.9); signed map (-12.7, -28.6). **Vector** length 73.7, 12.7% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.1 | +3.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.0 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +10.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.7 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | +0.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily F member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,186,095-184,194,012 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EST201864 |
| Gene groups (HGNC) | ATP binding cassette subfamily F |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUQ8](https://www.uniprot.org/uniprotkb/Q9NUQ8) (ATP-binding cassette sub-family F member 3):

> Displays an antiviral effect against flaviviruses such as west Nile virus (WNV) in the presence of OAS1B.

**Summary**, from NCBI Gene [55324](https://www.ncbi.nlm.nih.gov/gene/55324):

> This gene encodes a member of the ATP-binding cassette (ABC) transporter superfamily. ATP-binding cassette proteins transport various molecules across extra- and intracellular membranes. The protein encoded by this gene displays antiviral effect against flaviviruses. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:72](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:72) · Entrez [55324](https://www.ncbi.nlm.nih.gov/gene/55324) · UniProt [Q9NUQ8](https://www.uniprot.org/uniprotkb/Q9NUQ8) · Ensembl [ENSG00000161204](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161204)

## Data

Gene col 8421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8421); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8421]; `tensor/DDL_lfc|DDL_z.npy` [8421]; `embed/gene_vectors.npy` [8421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8421 or target_col == 8421). Every well: [[ABCF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
