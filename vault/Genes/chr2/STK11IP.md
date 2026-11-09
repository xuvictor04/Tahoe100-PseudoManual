---
symbol: "STK11IP"
type: "gene"
col: 6900
ensembl_id: "ENSG00000144589"
name: "serine/threonine kinase 11 interacting protein"
location: "2q35"
module: 127
arm: "+"
pooled_cpm: 9.45
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# STK11IP

*serine/threonine kinase 11 interacting protein* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.17× (z +6.4, q 6e-08, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.497× (z -11.0, q 2e-25, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK36]] (+0.63, fdr 1e-05), [[SETD4]] (+0.58, fdr 2e-05), [[YJU2]] (+0.57, fdr 1e-05); moves opposite to [[CBL]] (-0.51, fdr 1e-04), [[RALGPS2]] (-0.51, fdr 2e-04), [[BMP2K]] (-0.47, fdr 9e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +6.4 | 6e-08 | 19/48 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +6.4 | 6e-08 | 22/43 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.8 | 2e-04 | 15/46 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +4.8 | 2e-04 | 13/47 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 0.001 | 11/46 (NCI-H2030, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.011 | 3/48 (HCT15, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.037 | 14/47 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.041 | 12/47 (NCI-H2030, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.045 | 12/45 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.060 | 0/47 | top dose only | plate-row cell shift; position effect removed |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.15× | +3.1 | 0.11 | 1/48 (NCI-H1573) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.497×** | -11.0 | 2e-25 | 37/47 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -8.7 | 1e-15 | 24/43 (J82, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.609×** | -7.8 | 1e-12 | 27/47 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.610×** | -7.8 | 1e-12 | 28/47 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.647×** | -6.8 | 9e-10 | 22/43 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -6.7 | 2e-09 | 27/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -6.4 | 2e-08 | 17/45 (SW1417, RPMI-7951, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -6.3 | 2e-08 | 24/43 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.769×** | -5.8 | 4e-07 | 24/47 (C32, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.752×** | -4.3 | 9e-04 | 9/18 (LOX-IMVI, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.599×** | -4.2 | 0.001 | 13/48 (A549, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.778×** | -4.0 | 0.004 | 10/47 (RKO, RPMI-7951, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **0.791×** | -3.5 | 0.018 | 12/38 (SNU-423, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.858× | -3.4 | 0.028 | 13/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.028 | 12/44 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.806×** | -3.2 | 0.049 | 9/45 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 0.869× | -3.1 | 0.059 | 2/48 (A-427, NCI-H1573) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.814×** | -3.1 | 0.071 | 8/47 (SW 1088, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.58 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0870× (z -10.0) |
| [[HS-578T (line)]] | alt | 9.70 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~72% of this change |
| [[LOX-IMVI (line)]] | wt | 9.24 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[NCI-H2347 (line)]] | alt | 8.15 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.186× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.161× (z -9.3) |
| [[SNU-423 (line)]] | alt | 9.23 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.125× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK36]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[SETD4]] | +0.58 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[YJU2]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[FIZ1]] | +0.56 | +0.35 / +0.70 | both halves | 1e-04 |  |
| [[DMAP1]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PGAP3]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[MED24]] | +0.54 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TEN1]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ATXN7L2]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[RNF40]] | +0.53 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[VPS11]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[KAT5]] | +0.53 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBL]] | -0.51 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[RALGPS2]] | -0.51 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[BMP2K]] | -0.47 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[WWC2]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.9, 12.6); signed map (-10.3, -29.8). **Vector** length 59.7, 8.40% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | -2.9 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.8 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 11 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,597,857-219,616,451 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LIP1, KIAA1898, LKB1IP, STK11IP1 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1F8](https://www.uniprot.org/uniprotkb/Q8N1F8) (Serine/threonine-protein kinase 11-interacting protein):

> May regulate STK11/LKB1 function by controlling its subcellular localization.

**Summary**, from NCBI Gene [114790](https://www.ncbi.nlm.nih.gov/gene/114790):

> Enables protein kinase binding activity. Involved in intracellular protein localization. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19184) · Entrez [114790](https://www.ncbi.nlm.nih.gov/gene/114790) · UniProt [Q8N1F8](https://www.uniprot.org/uniprotkb/Q8N1F8) · Ensembl [ENSG00000144589](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144589)

## Data

Gene col 6900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6900); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6900]; `tensor/DDL_lfc|DDL_z.npy` [6900]; `embed/gene_vectors.npy` [6900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6900 or target_col == 6900). Every well: [[STK11IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK11IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
