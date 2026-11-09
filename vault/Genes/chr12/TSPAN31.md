---
symbol: "TSPAN31"
type: "gene"
col: 5707
ensembl_id: "ENSG00000135452"
name: "tetraspanin 31"
location: "12q14.1"
module: 77
arm: "-"
pooled_cpm: 12.83
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TSPAN31

*tetraspanin 31* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +13.9, q 2e-41, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.586× (z -8.5, q 1e-14, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R11]] (+0.66, fdr 1e-05), [[MED29]] (+0.64, fdr 1e-05), [[GPR108]] (+0.62, fdr 1e-05); moves opposite to [[HERC2P9]] (-0.67, fdr 7e-06), [[HERC2P3]] (-0.62, fdr 1e-05), [[ZNF692]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +13.9 | 2e-41 | 38/43 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +13.2 | 3e-37 | 30/35 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +11.2 | 1e-26 | 15/24 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +9.1 | 2e-17 | 27/45 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +9.0 | 3e-17 | 18/28 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +8.0 | 9e-14 | 8/47 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +6.6 | 4e-09 | 24/45 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.48×** | +6.2 | 4e-08 | 26/45 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.7 | 9e-07 | 22/47 (AsPC-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 2e-04 | 18/46 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 15/47 (A498, A-172, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.005 | 6/46 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.005 | 8/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.007 | 13/43 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.007 | 17/46 (SW480, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Thymol (drug)]] 5 µM |  | 1.17× | +3.5 | 0.015 | 8/47 (CHP-212, SHP-77, …) | rises with dose | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.033 | 5/46 (KATO III, BT-474, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.055 | 6/47 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.084 | 2/44 (HOP62, CFPAC-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.586×** | -8.5 | 1e-14 | 29/45 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.622×** | -7.6 | 1e-11 | 27/43 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -7.5 | 1e-11 | 28/45 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -7.3 | 3e-11 | 28/47 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.628×** | -7.0 | 3e-10 | 21/45 (Panc 03.27, BT-474, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.665×** | -6.5 | 8e-09 | 22/45 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.694×** | -5.8 | 5e-07 | 16/44 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -5.6 | 1e-06 | 20/40 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.709×** | -5.2 | 1e-05 | 23/44 (SK-MEL-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.561×** | -4.8 | 8e-05 | 17/43 (NCI-H460, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.749×** | -4.6 | 2e-04 | 16/45 (SW480, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -4.4 | 5e-04 | 12/46 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.753×** | -4.4 | 6e-04 | 17/45 (HOP62, SNU-1, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.812×** | -3.3 | 0.035 | 10/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.827×** | -3.0 | 0.092 | 3/47 (BT-474, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 24.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -10.3) ⚠ toxic · without an alert: [[Penfluridol (drug)]] 5 µM 0.158× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 8.56 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 9.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +8.6) | — |
| [[A498 (line)]] | wt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.4) |
| [[H4 (line)]] | wt | 13.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0386× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -9.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -10.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.177× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.1) | — |
| [[A-427 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R11]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[MED29]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[GPR108]] | +0.62 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[SSPN]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LAMTOR3]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PDCL3P4]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[RAP2C]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CAPNS1]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MAP3K20-AS1]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[IFNAR1]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P9]] | -0.67 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[HERC2P3]] | -0.62 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZNF692]] | -0.61 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[HERC2P2]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[NUP85]] | -0.60 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[CHST10]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[BRF1]] | -0.59 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[PPIH]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[WRN]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ASB13]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[CEP85]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (23.8, -36.0); signed map (14.9, -4.6). **Vector** length 77.2, 13.7% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[palbociclib (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.3 | -0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -8.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -6.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -7.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,738,013-57,750,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SAS |
| Gene groups (HGNC) | Tetraspanin family |
| Matched by | ensembl_id |

UniProt [Q12999](https://www.uniprot.org/uniprotkb/Q12999) carries no function annotation.

**Summary**, from NCBI Gene [6302](https://www.ncbi.nlm.nih.gov/gene/6302):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is thought to be involved in growth-related cellular processes. This gene is associated with tumorigenesis …

**Accessions** — [HGNC:10539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10539) · Entrez [6302](https://www.ncbi.nlm.nih.gov/gene/6302) · UniProt [Q12999](https://www.uniprot.org/uniprotkb/Q12999) · Ensembl [ENSG00000135452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135452)

## Data

Gene col 5707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5707); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5707]; `tensor/DDL_lfc|DDL_z.npy` [5707]; `embed/gene_vectors.npy` [5707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5707 or target_col == 5707). Every well: [[TSPAN31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
