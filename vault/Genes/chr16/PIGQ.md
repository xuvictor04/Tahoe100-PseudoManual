---
symbol: "PIGQ"
type: "gene"
col: 150
ensembl_id: "ENSG00000007541"
name: "phosphatidylinositol glycan anchor biosynthesis class Q"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 4.31
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# PIGQ

*phosphatidylinositol glycan anchor biosynthesis class Q* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.48× (z +10.3, q 5e-22, up in 38 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0754×; ⚠ cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0636×); [[Erlotinib (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0365×); [[Lapatinib ditosylate (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0706×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC14]] (+0.63, fdr 1e-05), [[WRAP73]] (+0.62, fdr 1e-04), [[RPUSD1]] (+0.61, fdr 8e-05); moves opposite to [[C12orf57]] (-0.55, fdr 5e-05), [[LRP2BP]] (-0.53, fdr 3e-04), [[LNP1]] (-0.52, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +10.3 | 5e-22 | 38/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +10.2 | 5e-22 | 37/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.23×** | +9.1 | 2e-17 | 11/24 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +8.6 | 2e-15 | 32/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.85×** | +6.7 | 3e-09 | 5/9 (SW1417, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +6.1 | 1e-07 | 17/38 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.72×** | +5.7 | 1e-06 | 5/13 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.6 | 2e-06 | 9/26 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.6 | 3e-04 | 7/47 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.016 | 5/37 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.061 | 4/23 (A-172, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.2 | 0.068 | 1/12 (A-172) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.071 | 1/36 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.093 | 4/33 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +3.0 | 0.093 | 0/42 | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 150.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0754×; ⚠ cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0636×); [[Erlotinib (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0365×); [[Lapatinib ditosylate (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0706×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.813× | -3.3 | 0.23 | 9/38 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.579× | -3.2 | 0.23 | 9/38 (SW1417, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.755× | -3.2 | 0.23 | 5/46 (HCT15, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.758× | -3.2 | 0.23 | 13/46 (CHP-212, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.764× | -3.1 | 0.24 | 8/46 (SHP-77, AN3 CA, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 2.63 | 0 | 1 | — | [[Erlotinib (drug)]] 0.5 µM 0.0365× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 3.21 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0636× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0754× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.92 | 0 | 1 | — | [[Lapatinib ditosylate (drug)]] 0.05 µM 0.0706× (z -8.8) |
| [[A-172 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC14]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.62 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[RPUSD1]] | +0.61 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[STUB1]] | +0.61 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[BORCS8]] | +0.60 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[FAAP100]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 | STRING 633 |
| [[NAA40]] | +0.58 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[CHMP1A]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[KCTD17]] | +0.57 | +0.47 / +0.38 | both halves | 7e-05 |  |
| [[PIP5K1C]] | +0.56 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[EDC4]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[SNRNP25]] | +0.56 | +0.26 / +0.51 | both halves | 4e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf57]] | -0.55 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[LRP2BP]] | -0.53 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[LNP1]] | -0.52 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[SPX]] | -0.52 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[HLA-DMA]] | -0.51 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[LSMEM1]] | -0.50 | -0.23 / -0.36 | both halves | 5e-04 |  |
| [[CCDC181]] | -0.49 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[OOEP]] | -0.49 | -0.30 / -0.27 | both halves | 3e-04 |  |
| [[LINC01030]] | -0.48 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[BORCS7-ASMT]] | -0.48 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[NUFIP2]] | -0.47 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[EPHX1]] | -0.47 | -0.24 / -0.29 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.1, 0.0); signed map (-31.6, 2.3). **Vector** length 44.9, 5.09% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.2 | +8.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class Q |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:566,995-584,109 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hGPI1, GPI1 |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; Glycosylphosphatidylinositol-N-acetylglucosaminyltransferase complex |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRB3](https://www.uniprot.org/uniprotkb/Q9BRB3) (Phosphatidylinositol N-acetylglucosaminyltransferase subunit Q):

> Part of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase (GPI-GnT) complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to phosphatidylinositol and participates in the first step of GPI biosynthesis.

**Summary**, from NCBI Gene [9091](https://www.ncbi.nlm.nih.gov/gene/9091):

> This gene is involved in the first step in glycosylphosphatidylinositol (GPI)-anchor biosynthesis. The GPI-anchor is a glycolipid found on many blood cells and serves to anchor proteins to the cell surface. This gene encodes a N-acetylglucosaminyl transferase component that is part of the complex that catalyzes transfer of N-acetylglucosamine (GlcNAc) from UDP-GlcNAc to phosphatidylinositol (PI). Alternatively spliced transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:14135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14135) · Entrez [9091](https://www.ncbi.nlm.nih.gov/gene/9091) · UniProt [Q9BRB3](https://www.uniprot.org/uniprotkb/Q9BRB3) · Ensembl [ENSG00000007541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007541)

## Data

Gene col 150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 150); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 150]; `tensor/DDL_lfc|DDL_z.npy` [150]; `embed/gene_vectors.npy` [150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 150 or target_col == 150). Every well: [[PIGQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
