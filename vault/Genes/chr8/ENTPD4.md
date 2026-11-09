---
symbol: "ENTPD4"
type: "gene"
col: 12365
ensembl_id: "ENSG00000197217"
name: "ectonucleoside triphosphate diphosphohydrolase 4"
location: "8p21.3"
module: 51
arm: "-"
pooled_cpm: 57.59
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ENTPD4

*ectonucleoside triphosphate diphosphohydrolase 4* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.34× (z +4.5, q 0.004, up in 31 of 48 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.77×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.703× (z -7.7, q 1e-11, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.648× (z -6.7, q 7e-09, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO2]] (+0.62, fdr 1e-05), [[GGCX]] (+0.62, fdr 1e-05), [[DAP]] (+0.61, fdr 7e-06); moves opposite to [[EPC1]] (-0.66, fdr 7e-06), [[BPTF]] (-0.61, fdr 3e-05), [[GTF2H1]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12365.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.77×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +4.5 | 0.004 | 31/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.8 | 0.040 | 21/48 (SW480, SW 900, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.19 | 18/48 (NCI-H2030, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.19 | 16/49 (H4, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.23× | +3.1 | 0.19 | 21/48 (SW 900, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.703×** | -7.7 | 1e-11 | 32/48 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.648×** | -6.7 | 7e-09 | 35/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.756×** | -6.1 | 2e-07 | 31/48 (NCI-H2347, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.701×** | -5.3 | 2e-05 | 29/48 (NCI-H1792, H4, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.733×** | -4.8 | 2e-04 | 30/48 (C-33 A, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -4.7 | 3e-04 | 26/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.838× | -3.8 | 0.010 | 21/48 (KATO III, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -3.8 | 0.010 | 25/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.859× | -3.3 | 0.053 | 20/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.800×** | -3.3 | 0.053 | 22/49 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.081 | 20/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.809×** | -3.1 | 0.081 | 18/48 (COLO 205, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 60.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -13.7) |
| [[A498 (line)]] | wt | 83.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.429× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 83.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -8.6) |
| [[HS-578T (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 75.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 94.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -10.8) |
| [[A-427 (line)]] | wt | 53.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.77× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0722× (z -8.8) |
| [[H4 (line)]] | wt | 80.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 54.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SW 900 (line)]] | alt | 84.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 53.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO2]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[GGCX]] | +0.62 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[DAP]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[MXRA7]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PDIA4]] | +0.58 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[EXTL3]] | +0.58 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[P3H1]] | +0.57 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[EIF4E3]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TPMT]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[GSDMB]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MTFR1]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[P4HB]] | +0.55 | +0.61 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | -0.66 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[BPTF]] | -0.61 | -0.72 / -0.46 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.61 | -0.74 / -0.49 | both halves | 1e-05 |  |
| [[ZNF830]] | -0.60 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[INO80D]] | -0.60 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[C1orf131]] | -0.59 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[YJU2]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ADNP]] | -0.59 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[POLR3C]] | -0.58 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[NKAPD1]] | -0.58 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[ZFX]] | -0.57 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[MRFAP1L1]] | -0.56 | -0.63 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.3, 15.5); signed map (-53.4, 5.7). **Vector** length 92.8, 22.0% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +5.0 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.2 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.3 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.0 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.8 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.4 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleoside triphosphate diphosphohydrolase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:23,385,783-23,457,695 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LALP70, LAP70, KIAA0392, NTPDase-4, UDPase; previously LYSAL1 |
| Gene groups (HGNC) | Ectonucleoside triphosphate diphosphohydrolase family |
| Reactome | 3 pathways, smallest: Phosphate bond hydrolysis by NTPDase proteins; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y227](https://www.uniprot.org/uniprotkb/Q9Y227) (Ectonucleoside triphosphate diphosphohydrolase 4):

> [Isoform 1]: Catalyzes the hydrolysis of nucleoside triphosphates and diphosphates in a calcium- or magnesium-dependent manner, with a preference for pyrimidines. Preferentially hydrolyzes UTP and TTP. AMP, ADP, ATP and UMP are not substrates. Preferentially activated by Ca(2+) over Mg(2+).; [Isoform 2]: Has a broad substrate specificity with the ability of cleaving all nucleotide di- and triphosphates with the exception of adenosine di- and triphosphate (ADP and ATP). Preferentially hydrolyzes …

**Summary**, from NCBI Gene [9583](https://www.ncbi.nlm.nih.gov/gene/9583):

> This gene encodes a member of the apyrase protein family. Apyrases are enzymes that catalyze the hydrolysis of nucleotide diphosphates and triphosphates in a calcium or magnesium-dependent manner. The encoded protein is an endo-apyrase and may play a role in salvaging nucleotides from lysosomes. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and these isoforms may differ in divalent cation dependence and substrate specificity. [provided by …

**Accessions** — [HGNC:14573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14573) · Entrez [9583](https://www.ncbi.nlm.nih.gov/gene/9583) · UniProt [Q9Y227](https://www.uniprot.org/uniprotkb/Q9Y227) · Ensembl [ENSG00000197217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197217)

## Data

Gene col 12365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12365); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12365]; `tensor/DDL_lfc|DDL_z.npy` [12365]; `embed/gene_vectors.npy` [12365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12365 or target_col == 12365). Every well: [[ENTPD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTPD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
