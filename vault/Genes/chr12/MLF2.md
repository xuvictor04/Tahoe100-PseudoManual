---
symbol: "MLF2"
type: "gene"
col: 1596
ensembl_id: "ENSG00000089693"
name: "myeloid leukemia factor 2"
location: "12p13.31"
module: 42
arm: "+"
pooled_cpm: 44.52
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MLF2

*myeloid leukemia factor 2* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.52× (z +11.6, q 2e-28, up in 41 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +7.8, q 8e-13, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.762× (z -4.8, q 7e-04, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.359×, NCI-H23 0.402×, NCI-H2030 0.445×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAR1A]] (+0.66, fdr 7e-06), [[AMPD2]] (+0.65, fdr 1e-05), [[TIMM10B]] (+0.64, fdr 1e-05); moves opposite to [[RNF115]] (-0.66, fdr 1e-05), [[CRCP]] (-0.61, fdr 9e-06), [[GCFC2]] (-0.60, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.52×** | +11.6 | 2e-28 | 41/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.26×** | +9.8 | 2e-20 | 33/39 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.97×** | +7.8 | 8e-13 | 41/44 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.8 | 8e-13 | 36/48 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.70×** | +6.7 | 3e-09 | 39/46 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.66×** | +6.4 | 2e-08 | 40/48 (SW480, KATO III, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.58×** | +5.7 | 9e-07 | 33/48 (SW480, HEC-1-A, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.2 | 1e-05 | 35/48 (A-427, BT-474, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.50×** | +5.1 | 3e-05 | 33/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.42×** | +4.3 | 0.001 | 25/47 (A549, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 27/48 (NCI-H1792, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +3.5 | 0.025 | 25/47 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.055 | 20/48 (HT-29, C32, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.359×, NCI-H23 0.402×, NCI-H2030 0.445×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.762×** | -4.8 | 7e-04 | 30/48 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | 0.768× | -3.2 | 0.39 | 22/48 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.772× | -3.1 | 0.39 | 23/47 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 37.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 65.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 123 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 25.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[PANC-1 (line)]] | alt | 24.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 51.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.5) |
| [[A498 (line)]] | wt | 73.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A549 (line)]] | wt | 41.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[J82 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 57.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 48.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 73.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 45.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW48 (line)]] | wt | 39.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAR1A]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[AMPD2]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TIMM10B]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ORMDL3]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TMED4]] | +0.61 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[EFCAB14]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ESYT1]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PLOD1]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[NUCB1]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[PMPCA]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ZDHHC16]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.66 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[CRCP]] | -0.61 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[GCFC2]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[STAT5B]] | -0.60 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[DIS3L]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[JPX]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[LSM14A]] | -0.58 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[POLR3C]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PPIG]] | -0.58 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SCMH1]] | -0.57 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[SETD2]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.0, -25.3); signed map (-51.2, -3.5). **Vector** length 82.3, 21.3% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.7 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | +2.5 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.0 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +5.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | myeloid leukemia factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,747,996-6,767,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NTN4 |
| Gene groups (HGNC) | Myeloid leukemia factor family |
| Matched by | ensembl_id |

UniProt [Q15773](https://www.uniprot.org/uniprotkb/Q15773) carries no function annotation.

**Summary**, from NCBI Gene [8079](https://www.ncbi.nlm.nih.gov/gene/8079):

> Predicted to be involved in regulation of DNA-templated transcription. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7126) · Entrez [8079](https://www.ncbi.nlm.nih.gov/gene/8079) · UniProt [Q15773](https://www.uniprot.org/uniprotkb/Q15773) · Ensembl [ENSG00000089693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089693)

## Data

Gene col 1596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1596); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1596]; `tensor/DDL_lfc|DDL_z.npy` [1596]; `embed/gene_vectors.npy` [1596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1596 or target_col == 1596). Every well: [[MLF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
