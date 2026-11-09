---
symbol: "USP2"
type: "gene"
col: 439
ensembl_id: "ENSG00000036672"
name: "ubiquitin specific peptidase 2"
location: "11q23.3"
module: 83
arm: "-"
pooled_cpm: 2.34
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# USP2

*ubiquitin specific peptidase 2* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.69× (z +16.3, q 0e+00, up in 41 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.125×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.0558×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.0499×; ⚠ toxic); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HT-29 0.0829×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXO6]] (+0.73, fdr 7e-06), [[STARD5]] (+0.68, fdr 8e-06), [[MLF1]] (+0.67, fdr 1e-05); moves opposite to [[CSTF3]] (-0.69, fdr 2e-05), [[ANXA2R-OT1]] (-0.67, fdr 1e-05), [[WDR33]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CGN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.69×** | +16.3 | 0e+00 | 41/43 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.49×** | +16.1 | 0e+00 | 40/41 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.22×** | +13.2 | 1e-37 | 34/41 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.46×** | +9.9 | 4e-21 | 35/43 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +8.6 | 9e-16 | 24/41 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +7.4 | 1e-11 | 12/31 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +6.3 | 3e-08 | 19/32 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.98×** | +5.8 | 5e-07 | 13/34 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +5.4 | 5e-06 | 0/3 | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +5.2 | 9e-06 | 13/36 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +5.1 | 2e-05 | 11/22 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.9 | 4e-05 | 1/12 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.022 | 4/44 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.56×** | +3.4 | 0.030 | 3/30 (C-33 A, SW1417, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.049 | 8/38 (RKO, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 439.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.125×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.0558×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.0499×; ⚠ toxic); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HT-29 0.0829×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 5 µM |  | 0.744× | -3.3 | 0.46 | 15/42 (Hs 766T, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 12.0 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0558× (z -10.0) |
| [[PANC-1 (line)]] | alt | 2.28 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.93× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 5.45 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0691× (z -9.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW1417 (line)]] | alt | 2.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +8.9) | — |
| [[A-172 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.888 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.792 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.820 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.589 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.841 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.815 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.756 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO6]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[STARD5]] | +0.68 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[MLF1]] | +0.67 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[THRA]] | +0.64 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[YPEL2]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TPPP]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.62 | +0.34 / +0.48 | both halves | 1e-04 | pathway: Deubiquitination |
| [[TJP3]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[MAST3]] | +0.60 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | +0.60 | +0.30 / +0.39 | both halves | 2e-04 |  |
| [[SNN]] | +0.60 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TUFT1]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF3]] | -0.69 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ANXA2R-OT1]] | -0.67 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[WDR33]] | -0.67 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ACAD9]] | -0.67 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[DNAAF10]] | -0.66 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PBLD]] | -0.65 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[DUS2]] | -0.63 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[AVEN]] | -0.62 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[AP4S1]] | -0.61 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ALG8]] | -0.61 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[LINC01829]] | -0.61 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[EXOSC3]] | -0.61 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGN]] | B | CGN activity raises USP2's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without CGN | 0.025 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[TUFT1]] | C | TUFT1 activity raises USP2's level | lines that do not express TUFT1 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without TUFT1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with TERT; also absent: FZD5, GRHL1, DBNDD2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.8, 7.5); signed map (-0.9, 19.8). **Vector** length 59.9, 10.3% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +16.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +16.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +9.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +3.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,355,215-119,381,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBP41 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 11 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Regulation of TP53 Degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75604](https://www.uniprot.org/uniprotkb/O75604) (Ubiquitin carboxyl-terminal hydrolase 2):

> Hydrolase that deubiquitinates polyubiquitinated target proteins such as MDM2, MDM4 and CCND1. Isoform 1 and isoform 4 possess both ubiquitin-specific peptidase and isopeptidase activities (By similarity). Deubiquitinates MDM2 without reversing MDM2-mediated p53/TP53 ubiquitination and thus indirectly promotes p53/TP53 degradation and limits p53 activity. Has no deubiquitinase activity against p53/TP53. Prevents MDM2-mediated degradation of MDM4. Plays a role in the G1/S cell-cycle progression …

**Summary**, from NCBI Gene [9099](https://www.ncbi.nlm.nih.gov/gene/9099):

> This gene encodes a member of the family of de-ubiquitinating enzymes, which belongs to the peptidase C19 superfamily. The encoded protein is a ubiquitin-specific protease which is required for TNF-alpha (tumor necrosis factor alpha) -induced NF-kB (nuclear factor kB) signaling. This protein deubiquitinates polyubiquitinated target proteins such as fatty acid synthase, murine double minute 2 (MDM2), MDM4/MDMX and cyclin D1. MDM2 and MDM4 are negative regulators of the p53 tumor suppressor and …

**Accessions** — [HGNC:12618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12618) · Entrez [9099](https://www.ncbi.nlm.nih.gov/gene/9099) · UniProt [O75604](https://www.uniprot.org/uniprotkb/O75604) · Ensembl [ENSG00000036672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000036672)

## Data

Gene col 439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 439); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 439]; `tensor/DDL_lfc|DDL_z.npy` [439]; `embed/gene_vectors.npy` [439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 439 or target_col == 439). Every well: [[USP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
