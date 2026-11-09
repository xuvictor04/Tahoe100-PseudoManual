---
symbol: "MRPL16"
type: "gene"
col: 9384
ensembl_id: "ENSG00000166902"
name: "mitochondrial ribosomal protein L16"
location: "11q12.1"
module: 17
arm: "+"
pooled_cpm: 17.85
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MRPL16

*mitochondrial ribosomal protein L16* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.73× (z +13.7, q 7e-40, up in 38 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (KATO III 15.6×, LoVo 13.6×, SW 900 16.3×, HOP62 9.14×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 14.1×, SW 900 13.4×, KATO III 7.70×, NCI-H2030 5.50×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 6.36×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.672× (z -5.8, q 3e-06, down in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.102×, C32 0.256×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.228×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.341×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRAK1BP1]] (+0.65, fdr 1e-05), [[FAM98B]] (+0.64, fdr 7e-06), [[NDUFAF5]] (+0.63, fdr 9e-06); moves opposite to [[THUMPD3-AS1]] (-0.56, fdr 3e-05), [[EPHA1-AS1]] (-0.56, fdr 2e-05), [[TRIM72]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9384.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (KATO III 15.6×, LoVo 13.6×, SW 900 16.3×, HOP62 9.14×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 14.1×, SW 900 13.4×, KATO III 7.70×, NCI-H2030 5.50×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 6.36×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.73×** | +13.7 | 7e-40 | 38/41 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +11.9 | 3e-30 | 27/30 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +9.1 | 2e-17 | 27/33 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.8 | 1e-09 | 36/44 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.41×** | +3.6 | 0.042 | 22/43 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9384.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.102×, C32 0.256×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.228×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.341×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -5.8 | 3e-06 | 31/47 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 18.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.3× (z +13.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 15.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.1× (z +14.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 33.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.21× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 14.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.14× (z +13.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 19.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.30× (z +12.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.6× (z +17.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 29.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.16× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.81× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.7× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.16× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +10.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -18.0) |
| [[SW480 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.61× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK1BP1]] | +0.65 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[FAM98B]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.63 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[SAAL1]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ALKBH8]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[RBM45]] | +0.60 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[DNAJC19]] | +0.59 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[DLAT]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TRAPPC11]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SNX4]] | +0.58 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[CROT]] | +0.58 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ZNHIT6]] | +0.58 | +0.40 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THUMPD3-AS1]] | -0.56 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[EPHA1-AS1]] | -0.56 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[TRIM72]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[SLC9A5]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[LINC00672]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PLA2G12B]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[LRP2BP]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[SNX31]] | -0.51 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[SLC23A3]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[LINC01033]] | -0.50 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[LINC02936]] | -0.50 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[CPEB2-DT]] | -0.50 | -0.40 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.8, -1.8); signed map (-24.9, -17.5). **Vector** length 58.6, 10.7% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:59,806,140-59,810,778 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20484, PNAS-111, uL16m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9NX20](https://www.uniprot.org/uniprotkb/Q9NX20) carries no function annotation.

**Summary**, from NCBI Gene [54948](https://www.ncbi.nlm.nih.gov/gene/54948):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14476) · Entrez [54948](https://www.ncbi.nlm.nih.gov/gene/54948) · UniProt [Q9NX20](https://www.uniprot.org/uniprotkb/Q9NX20) · Ensembl [ENSG00000166902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166902)

## Data

Gene col 9384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9384); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9384]; `tensor/DDL_lfc|DDL_z.npy` [9384]; `embed/gene_vectors.npy` [9384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9384 or target_col == 9384). Every well: [[MRPL16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
