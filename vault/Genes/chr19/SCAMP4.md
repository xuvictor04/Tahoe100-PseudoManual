---
symbol: "SCAMP4"
type: "gene"
col: 13595
ensembl_id: "ENSG00000227500"
name: "secretory carrier membrane protein 4"
location: "19p13.3"
module: 172
arm: "+"
pooled_cpm: 20.04
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# SCAMP4

*secretory carrier membrane protein 4* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.62× (z +8.7, q 2e-15, up in 28 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +5.4, q 1e-05, up in 20 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.163×, NCI-H460 0.180×, LS 180 0.204×, BT-474 0.182×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 0.141×, KATO III 0.162×, C-33 A 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (SW48 0.176×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KHSRP]] (+0.64, fdr 7e-06), [[OPA3]] (+0.58, fdr 2e-05), [[TMEM222]] (+0.56, fdr 2e-05); moves opposite to [[RTRAF]] (-0.48, fdr 4e-05), [[SCOC]] (-0.46, fdr 3e-04), [[CSNK1G3]] (-0.45, fdr 2e-04).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.7 | 2e-15 | 28/44 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.0 | 7e-07 | 22/46 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.4 | 1e-05 | 20/47 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.1 | 4e-05 | 19/47 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 4e-05 | 20/47 (LoVo, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 21/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 5e-04 | 17/48 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.001 | 20/48 (SW1417, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.25×** | +4.2 | 0.001 | 9/48 (SW480, SNU-423, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 9/45 (Panc 03.27, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.005 | 14/47 (A498, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.010 | 17/48 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.012 | 8/47 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.015 | 9/47 (A-172, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.4 | 0.030 | 14/33 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.033 | 11/47 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Rifaximin (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.041 | 5/47 (hTERT-HPNE, BT-474, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.041 | 7/48 (A498, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.046 | 6/47 (NCI-H661, NCI-H2347, …) | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.046 | 11/46 (NCI-H460, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13595.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.163×, NCI-H460 0.180×, LS 180 0.204×, BT-474 0.182×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 0.141×, KATO III 0.162×, C-33 A 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (SW48 0.176×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Elagolix sodium (drug)]] 0.5 µM |  | 0.827× | -3.6 | 0.16 | 13/47 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.830× | -3.4 | 0.16 | 11/47 (SNU-423, HOP62, …) | top dose only |  |
| [[Torkinib (drug)]] 5 µM | ⚠ toxic | 0.714× | -3.3 | 0.16 | 12/44 (LS 180, C32, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[5-Azacytidine (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.21 | 10/47 (HT-29, NCI-H2030, …) | inconsistent across doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 0.892× | -3.1 | 0.22 | 4/48 (HCT15, HepG2/C3A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 22.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Hesperidin (drug)]] 5 µM 0.176× (z -8.6) |
| [[SW480 (line)]] | alt | 24.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.1) | — |
| [[A-172 (line)]] | wt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +8.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -13.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHSRP]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[OPA3]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[TMEM222]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CTDNEP1]] | +0.55 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[ADAT3]] | +0.54 | +0.56 / +0.38 | both halves | 6e-05 | STRING 446; ⚠ **readthrough risk**: ADAT3 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[WDR82]] | +0.53 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[PHYKPL]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[DNLZ]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[DOHH]] | +0.50 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[PPP6R2]] | +0.50 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[DEAF1]] | +0.49 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[DDX56]] | +0.49 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TNPO2]] | +0.49 | +0.53 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTRAF]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SCOC]] | -0.46 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[CSNK1G3]] | -0.45 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[ACP1]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[MDH1]] | -0.44 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[HLTF]] | -0.44 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[GOLIM4]] | -0.40 | -0.38 / -0.26 | both halves | 4e-04 |  |
| [[TOP2B]] | -0.39 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.7, 0.1); signed map (2.1, -5.7). **Vector** length 64.6, 9.70% of its response variance represented; |z| ≥ 3 in 708 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +3.6 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.9 | +0.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.5 | -0.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | secretory carrier membrane protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,905,214-1,926,013 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33847 |
| Gene groups (HGNC) | Secretory carrier membrane proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969E2](https://www.uniprot.org/uniprotkb/Q969E2) (Secretory carrier-associated membrane protein 4):

> Probably involved in membrane protein trafficking.

**Summary**, from NCBI Gene [113178](https://www.ncbi.nlm.nih.gov/gene/113178):

> Secretory carrier membrane proteins (SCAMPs) are widely distributed integral membrane proteins implicated in membrane trafficking. Most SCAMPs (e.g., SCAMP1; MIM 606911) have N-terminal cytoplasmic NPF (arg-pro-phe) repeats, 4 central transmembrane regions, and a short C-terminal cytoplasmic tail. These SCAMPs likely have a role in endocytosis that is mediated by their NPF repeats. Other SCAMPs, such as SCAMP4, lack the NPF repeats and are therefore unlikely to function in endocytosis (summary …

**Accessions** — [HGNC:30385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30385) · Entrez [113178](https://www.ncbi.nlm.nih.gov/gene/113178) · UniProt [Q969E2](https://www.uniprot.org/uniprotkb/Q969E2) · Ensembl [ENSG00000227500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227500)

## Data

Gene col 13595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13595); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13595]; `tensor/DDL_lfc|DDL_z.npy` [13595]; `embed/gene_vectors.npy` [13595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13595 or target_col == 13595). Every well: [[SCAMP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAMP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
