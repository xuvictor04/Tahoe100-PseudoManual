---
symbol: "DEXI"
type: "gene"
col: 11240
ensembl_id: "ENSG00000182108"
name: "Dexi homolog"
location: "16p13.13"
module: 3
arm: "+"
pooled_cpm: 9.83
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DEXI

*Dexi homolog* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +11.9, q 1e-29, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.561× (z -9.5, q 9e-19, down in 36 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SK-MEL-2 0.185×, NCI-H1573 0.193×, A498 0.363×, HS-578T 0.271×, …); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.180×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAF1]] (+0.67, fdr 1e-05), [[CCNQ]] (+0.65, fdr 3e-05), [[RNF4]] (+0.65, fdr 1e-05); moves opposite to [[TIA1]] (-0.63, fdr 1e-05), [[DZIP3]] (-0.60, fdr 1e-05), [[DCAF8]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +11.9 | 1e-29 | 40/43 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.82×** | +7.0 | 7e-10 | 29/47 (PANC-1, SW1417, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.74×** | +6.5 | 2e-08 | 30/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.62×** | +5.7 | 2e-06 | 26/47 (PANC-1, AsPC-1, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.4 | 7e-06 | 17/39 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +4.4 | 0.001 | 16/40 (SHP-77, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.69×** | +4.4 | 0.001 | 20/44 (LS 180, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.008 | 13/44 (MIA PaCa-2, RPMI-7951, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.45×** | +3.6 | 0.022 | 10/21 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.024 | 16/48 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.024 | 16/44 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.032 | 6/47 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.42×** | +3.4 | 0.035 | 12/46 (SK-MEL-2, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.040 | 8/44 (NCI-H1573, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.047 | 10/42 (RKO, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.080 | 8/44 (AsPC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11240.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SK-MEL-2 0.185×, NCI-H1573 0.193×, A498 0.363×, HS-578T 0.271×, …); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.180×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.561×** | -9.5 | 9e-19 | 36/46 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.676×** | -4.0 | 0.019 | 19/44 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.750× | -3.3 | 0.15 | 12/46 (HOP62, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.763× | -3.1 | 0.32 | 7/47 (HEC-1-A, C-33 A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.3) |
| [[A498 (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.9) |
| [[A549 (line)]] | wt | 8.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 9.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -8.8) |
| [[HOP62 (line)]] | alt | 8.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.8) |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.8) |
| [[LoVo (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 8.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 7.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.1) |
| [[SW480 (line)]] | alt | 9.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.5) | — |
| [[A-427 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF1]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.65 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[RNF4]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SOCS7]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RTL10]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[HIRA]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FOXK2]] | +0.65 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[EIF4ENIF1]] | +0.64 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[RABEPK]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MARK4]] | +0.63 | +0.34 / +0.72 | both halves | 1e-04 |  |
| [[SLC37A3]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.63 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[DCAF8]] | -0.59 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[GRIPAP1]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[USP16]] | -0.58 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[OCIAD1]] | -0.57 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SRSF10]] | -0.57 | -0.32 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-5.1, -18.4); signed map (-40.8, 0.7). **Vector** length 65.5, 11.8% of its response variance represented; |z| ≥ 3 in 660 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +11.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.2 | +6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.3 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Dexi homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:10,928,891-10,942,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MYLE |
| Matched by | ensembl_id |

UniProt [O95424](https://www.uniprot.org/uniprotkb/O95424) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:13267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13267) · Entrez [28955](https://www.ncbi.nlm.nih.gov/gene/28955) · UniProt [O95424](https://www.uniprot.org/uniprotkb/O95424) · Ensembl [ENSG00000182108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182108)

## Data

Gene col 11240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11240); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11240]; `tensor/DDL_lfc|DDL_z.npy` [11240]; `embed/gene_vectors.npy` [11240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11240 or target_col == 11240). Every well: [[DEXI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEXI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
