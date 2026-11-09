---
symbol: "DDX23"
type: "gene"
col: 10479
ensembl_id: "ENSG00000174243"
name: "DEAD-box helicase 23"
location: "12q13.12"
module: 7
arm: "+"
pooled_cpm: 43.17
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DDX23

*DEAD-box helicase 23* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.64× (z +15.7, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.687× (z -7.3, q 1e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UPF1]] (+0.70, fdr 7e-06), [[PRCC]] (+0.67, fdr 7e-06), [[SETD1A]] (+0.65, fdr 7e-06); moves opposite to [[AP1S2]] (-0.51, fdr 2e-05), [[ATP11B]] (-0.49, fdr 6e-05), [[TRIM36]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.64×** | +15.7 | 0e+00 | 47/49 (SW480, COLO 205, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.42×** | +12.6 | 4e-34 | 46/48 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +6.6 | 8e-09 | 33/46 (H4, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.61×** | +4.9 | 1e-04 | 24/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +4.7 | 3e-04 | 24/47 (A-172, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.002 | 18/47 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.006 | 16/48 (SW480, NCI-H2347, …) | top dose only |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.029 | 13/48 (RKO, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.031 | 11/48 (NCI-H460, LoVo, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.039 | 14/48 (HT-29, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.065 | 16/47 (NCI-H1573, A498, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.687×** | -7.3 | 1e-10 | 36/48 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.722×** | -6.4 | 6e-08 | 39/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.739×** | -5.9 | 6e-07 | 30/48 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -5.9 | 6e-07 | 23/48 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.811×** | -5.8 | 1e-06 | 24/48 (SW480, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.773×** | -5.0 | 5e-05 | 26/48 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.766×** | -5.0 | 5e-05 | 24/48 (A-427, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.778×** | -4.9 | 7e-05 | 23/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -4.5 | 5e-04 | 24/48 (RKO, SW 900, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.2 | 0.002 | 23/47 (A-427, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.812×** | -4.1 | 0.002 | 19/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.864× | -4.0 | 0.003 | 12/48 (SNU-1, A-427, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.695×** | -3.7 | 0.009 | 18/48 (A-427, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.829×** | -3.7 | 0.010 | 17/48 (SW1417, KATO III, …) | all doses, flat | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.892× | -3.1 | 0.068 | 11/48 (A-427, HCT15, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 41.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.43× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.211× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 58.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.27× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 29.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | — |
| [[A-427 (line)]] | wt | 63.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 47.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.1) |
| [[COLO 205 (line)]] | alt | 67.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[LS 180 (line)]] | wt | 46.5 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.30× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 47.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.14× (z +9.4) | — |
| [[SW480 (line)]] | alt | 67.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.42× (z +14.5) | — |
| [[A549 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[AN3 CA (line)]] | alt | 47.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0963× (z -10.8) |
| [[C32 (line)]] | wt | 40.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -10.5) |
| [[LoVo (line)]] | wt | 60.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.51× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.60× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[NCI-H1792 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.10× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 53.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.37× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.109× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[SW48 (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A498 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPF1]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PRCC]] | +0.67 | +0.73 / +0.67 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 485 |
| [[SETD1A]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CHD8]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[DNAJC14]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PES1]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 | STRING 519 |
| [[THRAP3]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SUPT16H]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[BAP1]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[AKAP8]] | +0.58 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[ZC3H18]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 | STRING 410 |
| [[XRCC6]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S2]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ATP11B]] | -0.49 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[TRIM36]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ERO1B]] | -0.48 | -0.49 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-31.2, -10.0); signed map (-10.5, -28.5). **Vector** length 106, 24.8% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +11.2 | +15.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +10.0 | +12.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.3 | +6.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.6 | +4.7 |
|  | [[NG25 (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.7 | +2.4 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.5 | -4.9 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.4 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:48,829,756-48,852,842 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Prp28, U5-100KD, PRPF28, SNRNP100 |
| Gene groups (HGNC) | DEAD-box helicases; U5 small nuclear ribonucleoprotein |
| Reactome | 8 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing - Major Pathway; mRNA Splicing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUQ8](https://www.uniprot.org/uniprotkb/Q9BUQ8) (Probable ATP-dependent RNA helicase DDX23):

> Involved in pre-mRNA splicing and its phosphorylated form (by SRPK2) is required for spliceosomal B complex formation. Independently of its spliceosome formation function, required for the suppression of incorrect R-loops formed during transcription; R-loops are composed of a DNA:RNA hybrid and the associated non-template single-stranded DNA.

**Summary**, from NCBI Gene [9416](https://www.ncbi.nlm.nih.gov/gene/9416):

> This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, …

**Accessions** — [HGNC:17347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17347) · Entrez [9416](https://www.ncbi.nlm.nih.gov/gene/9416) · UniProt [Q9BUQ8](https://www.uniprot.org/uniprotkb/Q9BUQ8) · Ensembl [ENSG00000174243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174243)

## Data

Gene col 10479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10479); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10479]; `tensor/DDL_lfc|DDL_z.npy` [10479]; `embed/gene_vectors.npy` [10479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10479 or target_col == 10479). Every well: [[DDX23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
