---
symbol: "TIMM9"
type: "gene"
col: 1988
ensembl_id: "ENSG00000100575"
name: "translocase of inner mitochondrial membrane 9"
location: "14q23.1"
module: 1
arm: "+"
pooled_cpm: 14.93
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TIMM9

*translocase of inner mitochondrial membrane 9* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +11.3, q 1e-26, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.99× (z +10.6, q 1e-23, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.631× (z -7.1, q 8e-10, down in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.142×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.183×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Menadione (drug)]] 0.5 µM in 1 line (COLO 205 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR75]] (+0.72, fdr 7e-06), [[MRPL15]] (+0.68, fdr 8e-06), [[ESF1]] (+0.68, fdr 8e-06); moves opposite to [[NUCB1]] (-0.59, fdr 1e-05), [[KLHL25]] (-0.55, fdr 1e-05), [[APLP2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +11.3 | 1e-26 | 37/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +10.6 | 1e-23 | 35/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +10.1 | 1e-21 | 35/46 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +8.8 | 2e-16 | 31/42 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.4 | 1e-11 | 31/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +7.1 | 9e-11 | 26/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +6.6 | 4e-09 | 30/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.46×** | +5.8 | 6e-07 | 21/46 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.90×** | +4.8 | 1e-04 | 20/46 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +4.7 | 1e-04 | 23/46 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.35×** | +4.4 | 5e-04 | 14/28 (CFPAC-1, Hs 766T, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +4.1 | 0.002 | 15/45 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.30×** | +4.0 | 0.003 | 13/43 (A-172, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.30×** | +4.0 | 0.003 | 19/40 (A549, NCI-H460, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.003 | 10/47 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.67×** | +3.8 | 0.005 | 13/43 (SK-MEL-2, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.005 | 10/45 (A549, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.006 | 13/46 (LoVo, HS-578T, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.006 | 13/46 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.008 | 14/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.017 | 6/48 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.018 | 7/48 (NCI-H23, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.029 | 9/45 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1988.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.142×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.183×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Menadione (drug)]] 0.5 µM in 1 line (COLO 205 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -7.1 | 8e-10 | 30/47 (SNU-423, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -3.0 | 0.69 | 12/48 (HEC-1-A, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 10.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.12× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 16.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.184× (z -8.6) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 9.63 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.119× (z -9.1) |
| [[KATO III (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.183× (z -9.8) |
| [[A-172 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR75]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.68 | +0.57 / +0.73 | both halves | 8e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[ESF1]] | +0.68 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[MECR]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[THUMPD2]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MIOS]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[LIPT1]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.61 | +0.67 / +0.55 | both halves | 1e-05 | STRING 549 |
| [[GCFC2]] | +0.61 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ANGEL1]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCB1]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[KLHL25]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[APLP2]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PRDX1]] | -0.54 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[INPP5A]] | -0.53 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[MBOAT7]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SAR1A]] | -0.52 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-47.9, -8.2); signed map (-2.1, -39.6). **Vector** length 76.0, 14.1% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.3 | +11.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +7.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -7.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:58,408,495-58,427,531 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIM9A |
| Gene groups (HGNC) | TIM22 complex |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Mitochondrial protein import; Mitochondrial protein degradation; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5J7](https://www.uniprot.org/uniprotkb/Q9Y5J7) (Mitochondrial import inner membrane translocase subunit Tim9):

> Mitochondrial intermembrane chaperone that participates in the import and insertion of multi-pass transmembrane proteins into the mitochondrial inner membrane. May also be required for the transfer of beta-barrel precursors from the TOM complex to the sorting and assembly machinery (SAM complex) of the outer membrane. Acts as a chaperone-like protein that protects the hydrophobic precursors from aggregation and guide them through the mitochondrial intermembrane space.

**Summary**, from NCBI Gene [26520](https://www.ncbi.nlm.nih.gov/gene/26520):

> TIMM9 belongs to a family of evolutionarily conserved proteins that are organized in heterooligomeric complexes in the mitochondrial intermembrane space. These proteins mediate the import and insertion of hydrophobic membrane proteins into the mitochondrial inner membrane.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:11819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11819) · Entrez [26520](https://www.ncbi.nlm.nih.gov/gene/26520) · UniProt [Q9Y5J7](https://www.uniprot.org/uniprotkb/Q9Y5J7) · Ensembl [ENSG00000100575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100575)

## Data

Gene col 1988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1988); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1988]; `tensor/DDL_lfc|DDL_z.npy` [1988]; `embed/gene_vectors.npy` [1988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1988 or target_col == 1988). Every well: [[TIMM9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
