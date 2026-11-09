---
symbol: "BBIP1"
type: "gene"
col: 13200
ensembl_id: "ENSG00000214413"
name: "BBSome interacting protein 1"
location: "10q25.2"
module: 4
arm: "-"
pooled_cpm: 20.14
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# BBIP1

*BBSome interacting protein 1* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +12.0, q 2e-30, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.493× (z -6.3, q 1e-07, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCG27]] (+0.63, fdr 1e-05), [[SLC25A53]] (+0.61, fdr 3e-05), [[SWT1]] (+0.60, fdr 1e-05); moves opposite to [[RBM17]] (-0.59, fdr 1e-05), [[DLAT]] (-0.57, fdr 3e-05), [[SSRP1]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +12.0 | 2e-30 | 34/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +11.5 | 5e-28 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +11.1 | 3e-26 | 38/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +10.3 | 1e-22 | 31/46 (C32, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +9.4 | 8e-19 | 29/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 1e-07 | 26/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 0.001 | 10/47 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | **1.24×** | +4.1 | 0.003 | 15/40 (HT-29, A-172, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.23×** | +3.9 | 0.005 | 12/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **1.22×** | +3.3 | 0.052 | 10/30 (NCI-H460, NCI-H2030, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.493×** | -6.3 | 1e-07 | 23/45 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.737×** | -5.8 | 1e-06 | 23/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.742×** | -5.7 | 2e-06 | 20/46 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.769×** | -4.4 | 0.001 | 15/46 (LOX-IMVI, AN3 CA, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.034 | 7/47 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.673×** | -3.5 | 0.034 | 15/47 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.832×** | -3.5 | 0.034 | 16/47 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.4 | 0.049 | 14/47 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | 0.708× | -3.1 | 0.13 | 3/47 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.1 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.74× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 46.8 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +14.1) | — |
| [[SW1417 (line)]] | alt | 14.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[SW480 (line)]] | alt | 20.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.4) | — |
| [[A-172 (line)]] | wt | 25.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 16.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +9.5) | — |
| [[C32 (line)]] | wt | 16.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.72× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.191× (z -9.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCG27]] | +0.63 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A53]] | +0.61 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[SWT1]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[C16orf46]] | +0.59 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[TTC41P]] | +0.56 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[URM1]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PCF11-AS1]] | +0.55 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[RNASEK]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[CREM]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[TPTE2]] | +0.53 | +0.52 / +0.29 | both halves | 2e-04 |  |
| [[ZBTB8OS]] | +0.52 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[UXT]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM17]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[DLAT]] | -0.57 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SSRP1]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MCMBP]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SCAP]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[AKAP1]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[COG2]] | -0.52 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[PPA1]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[AHCTF1]] | -0.50 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[SNX18]] | -0.50 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[MRPL3]] | -0.50 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TRAP1]] | -0.49 | -0.39 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises BBIP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.5, -37.7); signed map (-0.7, 8.6). **Vector** length 83.5, 16.7% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.6 | +11.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +11.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.5 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | BBSome interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:110,898,730-110,919,201 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA348N5.3, BBIP10, BBS18; previously NCRNA00081 |
| Gene groups (HGNC) | BBSome |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MTZ0](https://www.uniprot.org/uniprotkb/A8MTZ0) (BBSome-interacting protein 1):

> The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane. Firstly the BBSome associates with the …

**Summary**, from NCBI Gene [92482](https://www.ncbi.nlm.nih.gov/gene/92482):

> This gene encodes one of eight proteins that form the BBSome complex and is essential for its assembly. The BBSome complex is involved in trafficking signal receptors to and from the cilia. Mutations in this gene result in Bardet-Biedl syndrome 18. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:28093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28093) · Entrez [92482](https://www.ncbi.nlm.nih.gov/gene/92482) · UniProt [A8MTZ0](https://www.uniprot.org/uniprotkb/A8MTZ0) · Ensembl [ENSG00000214413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214413)

## Data

Gene col 13200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13200); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13200]; `tensor/DDL_lfc|DDL_z.npy` [13200]; `embed/gene_vectors.npy` [13200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13200 or target_col == 13200). Every well: [[BBIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
