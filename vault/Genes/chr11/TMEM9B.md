---
symbol: "TMEM9B"
type: "gene"
col: 10599
ensembl_id: "ENSG00000175348"
name: "TMEM9 domain family member B"
location: "11p15.4"
module: 29
arm: "+"
pooled_cpm: 15.35
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# TMEM9B

*TMEM9 domain family member B* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.39× (z +13.4, q 2e-38, up in 43 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.145×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Nimesulide (drug)]] 5 µM in 1 line (RKO 0.224×; ⚠ toxic; unreliable plate only); [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.139×; ⚠ transcription drop; cell-cycle shift, explains ~26% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.219×); [[Cepharanthine (drug)]] 5 µM in 1 line (SHP-77 0.280×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPC]] (+0.61, fdr 1e-05), [[DR1]] (+0.59, fdr 2e-05), [[THAP12]] (+0.58, fdr 1e-05); moves opposite to [[GOLGA6L9]] (-0.59, fdr 1e-05), [[UPF3B]] (-0.50, fdr 5e-05), [[ATF4]] (-0.48, fdr 6e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.39×** | +13.4 | 2e-38 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +10.3 | 2e-22 | 31/47 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.79×** | +10.1 | 1e-21 | 25/37 (PANC-1, A549, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +8.9 | 8e-17 | 31/43 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +7.2 | 6e-11 | 26/43 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.57×** | +7.2 | 6e-11 | 19/28 (PANC-1, hTERT-HPNE, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.45×** | +6.2 | 4e-08 | 14/28 (PANC-1, hTERT-HPNE, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.37×** | +5.5 | 3e-06 | 19/48 (NCI-H1573, PANC-1, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.32×** | +4.8 | 8e-05 | 14/42 (LS 180, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +4.5 | 4e-04 | 13/47 (HT-29, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.4 | 5e-04 | 10/21 (SW480, A-172, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.003 | 12/47 (SW48, A-172, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.003 | 5/44 (PANC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.016 | 8/45 (HCT15, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.032 | 5/42 (A-172, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.036 | 6/47 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.036 | 11/48 (HOP62, A-172, …) | top dose only |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.036 | 5/46 (NCI-H2347, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10599.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.145×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Nimesulide (drug)]] 5 µM in 1 line (RKO 0.224×; ⚠ toxic; unreliable plate only); [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.139×; ⚠ transcription drop; cell-cycle shift, explains ~26% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.219×); [[Cepharanthine (drug)]] 5 µM in 1 line (SHP-77 0.280×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[SBI-0640756 (drug)]] 5 µM |  | 0.665× | -3.7 | 0.10 | 10/44 (SK-MEL-2, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[RKO (line)]] | wt | 20.3 | 0 | 2 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.224× (z -10.1) ⚠ toxic; unreliable plate only · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.219× (z -9.5) |
| [[SW480 (line)]] | alt | 21.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +13.5) | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -11.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.139× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 9.93 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.280× (z -8.5) |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPC]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[DR1]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[THAP12]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CUL2]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[C6orf120]] | +0.56 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ADAT1]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[UQCRFS1]] | +0.53 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ERH]] | +0.53 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[ATRAID]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[MUL1]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[COPS3]] | +0.52 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[SF3B4]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA6L9]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[UPF3B]] | -0.50 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ATF4]] | -0.48 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[MALAT1]] | -0.45 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[DOCK6]] | -0.45 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[SNHG12]] | -0.44 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[ABAT]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SNHG6]] | -0.44 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[EEF1D]] | -0.44 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[CROCCP2-1]] | -0.44 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[SNHG7]] | -0.44 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[RAB13]] | -0.44 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-18.0, -15.2); signed map (-21.7, -42.7). **Vector** length 69.9, 11.5% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +13.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +4.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | TMEM9 domain family member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:8,947,202-8,965,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C11orf15 |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ34](https://www.uniprot.org/uniprotkb/Q9NQ34) (Transmembrane protein 9B):

> Enhances production of pro-inflammatory cytokines induced by TNF, IL1B, and TLR ligands. Has a role in TNF activation of both the NF-kappaB and MAPK pathways.

**Summary**, from NCBI Gene [56674](https://www.ncbi.nlm.nih.gov/gene/56674):

> Involved in positive regulation of canonical NF-kappaB signal transduction. Located in early endosome membrane and lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1168) · Entrez [56674](https://www.ncbi.nlm.nih.gov/gene/56674) · UniProt [Q9NQ34](https://www.uniprot.org/uniprotkb/Q9NQ34) · Ensembl [ENSG00000175348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175348)

## Data

Gene col 10599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10599); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10599]; `tensor/DDL_lfc|DDL_z.npy` [10599]; `embed/gene_vectors.npy` [10599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10599 or target_col == 10599). Every well: [[TMEM9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
