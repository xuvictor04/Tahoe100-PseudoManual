---
symbol: "USP21"
type: "gene"
col: 6706
ensembl_id: "ENSG00000143258"
name: "ubiquitin specific peptidase 21"
location: "1q23.3"
module: 153
arm: "+"
pooled_cpm: 8.47
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# USP21

*ubiquitin specific peptidase 21* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.94× (z +8.4, q 3e-14, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.709× (z -6.2, q 3e-07, down in 21 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC119B]] (+0.60, fdr 1e-05), [[STRN4]] (+0.60, fdr 1e-05), [[USP19]] (+0.58, fdr 1e-05); moves opposite to [[ARPC2]] (-0.50, fdr 8e-05), [[UBTD2]] (-0.48, fdr 5e-05), [[LINC01019]] (-0.47, fdr 3e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +8.4 | 3e-14 | 30/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +7.7 | 5e-12 | 21/38 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +6.9 | 8e-10 | 13/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +6.6 | 5e-09 | 17/44 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.6 | 6e-09 | 23/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +5.9 | 3e-07 | 25/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.1 | 3e-05 | 17/39 (NCI-H23, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 0.002 | 12/46 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.069 | 8/42 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.2 | 0.073 | 1/28 (C32) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -6.2 | 3e-07 | 21/41 (LS 180, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.644×** | -5.6 | 6e-06 | 25/47 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.686×** | -4.8 | 3e-04 | 16/47 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -4.6 | 8e-04 | 10/18 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -4.2 | 0.003 | 14/47 (C32, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.746×** | -3.7 | 0.018 | 15/47 (NCI-H460, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.021 | 13/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.784× | -3.1 | 0.13 | 8/47 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.24 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0843× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[Hs 766T (line)]] | wt | 7.03 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.106× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.18× (z +8.9) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 8.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 9.25 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0676× (z -9.8) |
| [[SW48 (line)]] | wt | 10.3 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0768× (z -9.6) |
| [[A-172 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC119B]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[STRN4]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[USP19]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 | same gene group; pathway: Deubiquitination |
| [[AJM1]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[WDR6]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[CRTC2]] | +0.56 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[ZBTB39]] | +0.53 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[FOXJ2]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[PANK4]] | +0.53 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZBED6]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[WASH9P]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TARBP2]] | +0.51 | +0.34 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC2]] | -0.50 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[UBTD2]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[LINC01019]] | -0.47 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CHCHD2]] | -0.47 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[RAP1B]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ARHGEF18]] | -0.46 | -0.43 / -0.38 | both halves | 6e-05 | pathway: Death Receptor Signaling |
| [[CSNK1A1]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RAB7A]] | -0.45 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[TPM4]] | -0.45 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[ZSWIM6]] | -0.44 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[KHDRBS1]] | -0.44 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[UCHL3]] | -0.43 | -0.34 / -0.30 | both halves | 2e-04 | pathway: Deubiquitination; STRING 745 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises USP21's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises USP21's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, -23.3); signed map (-10.6, -32.5). **Vector** length 57.0, 7.62% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.7 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.7 | +6.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.8 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,159,450-161,165,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | USP16; previously USP23 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 7 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Regulation of TNFR1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK80](https://www.uniprot.org/uniprotkb/Q9UK80) (Ubiquitin carboxyl-terminal hydrolase 21):

> Deubiquitinates histone H2A, a specific tag for epigenetic transcriptional repression, thereby acting as a coactivator (By similarity). Deubiquitination of histone H2A releaves the repression of di- and trimethylation of histone H3 at 'Lys-4', resulting in regulation of transcriptional initiation (By similarity). Regulates gene expression via histone H2A deubiquitination (By similarity). Deubiquitinates BAZ2A/TIP5 leading to its stabilization. Also capable of removing NEDD8 from NEDD8 …

**Summary**, from NCBI Gene [27005](https://www.ncbi.nlm.nih.gov/gene/27005):

> This gene encodes a member of the C19 peptidase family, also known as family 2 of ubiquitin carboxy-terminal hydrolases. The encoded protein cleaves ubiquitin from ubiquitinated proteins for recycling in intracellular protein degradation. The encoded protein is also able to release NEDD8, a ubiquitin-like protein, from NEDD8-conjugated proteins. This gene has been referred to as USP16 and USP23 but is now known as USP21. Alternatively spliced transcript variants encoding different isoforms have …

**Accessions** — [HGNC:12620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12620) · Entrez [27005](https://www.ncbi.nlm.nih.gov/gene/27005) · UniProt [Q9UK80](https://www.uniprot.org/uniprotkb/Q9UK80) · Ensembl [ENSG00000143258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143258)

## Data

Gene col 6706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6706); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6706]; `tensor/DDL_lfc|DDL_z.npy` [6706]; `embed/gene_vectors.npy` [6706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6706 or target_col == 6706). Every well: [[USP21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
