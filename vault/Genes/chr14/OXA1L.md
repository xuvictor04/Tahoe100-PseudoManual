---
symbol: "OXA1L"
type: "gene"
col: 7896
ensembl_id: "ENSG00000155463"
name: "OXA1L mitochondrial inner membrane insertase"
location: "14q11.2"
module: 29
arm: "+"
pooled_cpm: 21.34
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# OXA1L

*OXA1L mitochondrial inner membrane insertase* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.86× (z +9.9, q 2e-20, up in 34 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belzutifan (drug)]] 5 µM: 1.65× (z +4.1, q 0.005, up in 15 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.816× (z -4.6, q 0.002, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.0595×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.188×; ⚠ toxic; cell-cycle shift, explains ~61% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.313×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLST8]] (+0.58, fdr 2e-05), [[UQCRC1]] (+0.57, fdr 3e-05, ⚠ UQCRC1 in the vector space only through flagged drug-doses), [[ATP5F1C]] (+0.57, fdr 3e-05), [[GPS1]] (+0.56, fdr 1e-05); moves opposite to [[CACNG8]] (-0.51, fdr 5e-05), [[GSK3B-DT]] (-0.51, fdr 8e-05), [[LINC01772]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.86×** | +9.9 | 2e-20 | 34/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.88×** | +9.7 | 6e-20 | 26/32 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.41×** | +5.5 | 9e-06 | 24/45 (CFPAC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.54×** | +5.1 | 5e-05 | 20/35 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.65×** | +4.1 | 0.005 | 15/45 (HS-578T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.007 | 14/46 (NCI-H1573, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.28×** | +3.9 | 0.008 | 16/48 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.008 | 17/48 (NCI-H2030, SW480, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.008 | 12/48 (NCI-H2347, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +3.8 | 0.008 | 18/47 (HepG2/C3A, C-33 A, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.021 | 8/48 (SW480, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.16× | +3.3 | 0.038 | 10/48 (NCI-H460, HCT15, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.040 | 10/48 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.058 | 8/48 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.087 | 13/47 (NCI-H1792, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.0595×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.188×; ⚠ toxic; cell-cycle shift, explains ~61% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.313×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.816×** | -4.6 | 0.002 | 21/47 (hTERT-HPNE, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.817× | -3.3 | 0.32 | 9/47 (SNU-423, HOP62, …) | top dose only |  |
| [[Baicalin (drug)]] 5 µM |  | 0.877× | -3.0 | 0.43 | 9/48 (NCI-H1792, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.8) |
| [[LoVo (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0595× (z -15.0) |
| [[A-172 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLST8]] | +0.58 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[UQCRC1]] ⚠ | +0.57 | +0.44 / +0.48 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 504; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1C]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[GPS1]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[FAM210B]] | +0.55 | +0.60 / +0.32 | both halves | 2e-04 |  |
| [[ABHD14B]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ABRAXAS1]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[APEX1]] | +0.52 | +0.57 / +0.44 | both halves | 3e-05 | STRING 608 |
| [[SUMF2]] | +0.51 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[MRPL37]] | +0.51 | +0.56 / +0.43 | both halves | 3e-05 | pathway: Mitochondrial ribosome-associated quality control; STRING 861 |
| [[PYURF]] | +0.51 | +0.44 / +0.44 | both halves | 3e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[PLA2G12A]] | +0.51 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[TSPAN6]] | +0.50 | +0.56 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNG8]] | -0.51 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[GSK3B-DT]] | -0.51 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[LINC01772]] | -0.49 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[RIPK1]] | -0.47 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[BCL10-AS1]] | -0.44 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[LINC02798]] | -0.44 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[MIRLET7IHG]] | -0.44 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[TLNRD1]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[LINC03016]] | -0.43 | -0.38 / -0.25 | both halves | 4e-04 |  |
| [[ADGRL1-AS1]] | -0.43 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[PROSER2-AS1]] | -0.43 | -0.39 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.1, -17.3); signed map (-36.7, -28.9). **Vector** length 50.9, 7.75% of its response variance represented; |z| ≥ 3 in 536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | +1.8 | +3.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +1.7 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +1.7 | +9.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -3.3 |
|  | [[AT7519 (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | OXA1L mitochondrial inner membrane insertase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,766,522-22,773,042 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC133129, OXA1, OXA1L1 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex I biogenesis; Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15070](https://www.uniprot.org/uniprotkb/Q15070) (Mitochondrial inner membrane protein OXA1L):

> Mitochondrial membrane insertase that mediates the cotranslational insertion of integral membrane proteins into the mitochondrial inner membrane. Essential for the activity and assembly of cytochrome oxidase. Required for the correct biogenesis of ATP synthase and complex I in mitochondria.

**Summary**, from NCBI Gene [5018](https://www.ncbi.nlm.nih.gov/gene/5018):

> This gene encodes an evolutionarily conserved protein that is localized to the inner mitochondrial membrane. The encoded protein is essential for the translocation of the N-terminal tail of subunit 2 of cytochrome c oxidase, and is involved in the assembly of the cytochrome c oxidase and ATPase complexes of the mitochondrial respiratory chain. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:8526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8526) · Entrez [5018](https://www.ncbi.nlm.nih.gov/gene/5018) · UniProt [Q15070](https://www.uniprot.org/uniprotkb/Q15070) · Ensembl [ENSG00000155463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155463)

## Data

Gene col 7896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7896); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7896]; `tensor/DDL_lfc|DDL_z.npy` [7896]; `embed/gene_vectors.npy` [7896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7896 or target_col == 7896). Every well: [[OXA1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXA1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
