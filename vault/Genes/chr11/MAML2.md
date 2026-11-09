---
symbol: "MAML2"
type: "gene"
col: 11530
ensembl_id: "ENSG00000184384"
name: "mastermind like transcriptional coactivator 2"
location: "11q21"
module: 70
arm: "+"
pooled_cpm: 342.76
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 58
n_dd_up_clean: 0
n_dd_down_clean: 41
in_vector_space: true
direction_upstream: 11
direction_downstream: 23
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# MAML2

*mastermind like transcriptional coactivator 2* — 11q21

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 4.72×, HOP62 2.37×, HT-29 2.65×, A-172 1.81×; ⚠ cell-cycle shift, explains ~76% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (HOP62 3.32×, PANC-1 2.58×, A-172 2.33×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 5 µM in 2 lines (HS-578T 3.03×, hTERT-HPNE 2.75×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (HS-578T 3.11×); [[Digitoxin (drug)]] 0.5 µM in 1 line (A-172 2.28×).
> Pooled over the cell lines (median), lowered significantly by 58 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.388× (z -18.0, q 0e+00, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK6]] (+0.57, fdr 1e-05), [[TGFBR2]] (+0.56, fdr 1e-05), [[IKBKE]] (+0.56, fdr 2e-05); moves opposite to [[CLCC1]] (-0.56, fdr 1e-05), [[XPOT]] (-0.51, fdr 3e-05), [[TPD52L2]] (-0.50, fdr 3e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ITGA1]] → it (grade B ⚠); 23 go from it, the strongest it → [[TGFBR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11530.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 4.72×, HOP62 2.37×, HT-29 2.65×, A-172 1.81×; ⚠ cell-cycle shift, explains ~76% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (HOP62 3.32×, PANC-1 2.58×, A-172 2.33×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 5 µM in 2 lines (HS-578T 3.03×, hTERT-HPNE 2.75×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (HS-578T 3.11×); [[Digitoxin (drug)]] 0.5 µM in 1 line (A-172 2.28×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 1.20× | +3.4 | 0.23 | 17/40 (SW1417, HS-578T, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.23 | 15/40 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.2 | 0.23 | 1/42 (MIA PaCa-2) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.24 | 19/40 (A549, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 58 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.388×** | -18.0 | 0e+00 | 39/41 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -13.7 | 3e-40 | 31/37 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.367×** | -13.5 | 3e-39 | 36/40 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.369×** | -13.4 | 6e-39 | 36/40 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.464×** | -10.3 | 5e-23 | 34/40 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -10.3 | 5e-23 | 34/39 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.439×** | -10.2 | 1e-22 | 32/37 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.476×** | -10.0 | 1e-21 | 35/40 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.477×** | -10.0 | 1e-21 | 37/40 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.468×** | -9.8 | 5e-21 | 33/39 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.484×** | -9.8 | 9e-21 | 35/40 (LoVo, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.500×** | -9.3 | 5e-19 | 33/40 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.429×** | -9.1 | 4e-18 | 33/41 (Panc 03.27, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.637×** | -8.6 | 4e-16 | 37/41 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.559×** | -7.4 | 5e-12 | 33/40 (HepG2/C3A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -6.8 | 3e-10 | 32/40 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.603×** | -6.8 | 3e-10 | 33/40 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -6.6 | 1e-09 | 34/42 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.617×** | -6.5 | 2e-09 | 34/40 (KATO III, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.416×** | -6.2 | 2e-08 | 32/40 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.658×** | -5.6 | 5e-07 | 32/41 (KATO III, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 1,189 | 0 | 26 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -28.1) |
| [[KATO III (line)]] | alt | 1,196 | 0 | 23 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -24.6) |
| [[LoVo (line)]] | wt | 352 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -23.1) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -16.1) |
| [[LS 180 (line)]] | wt | 309 | 0 | 19 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 882 | 0 | 18 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -17.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -15.8) |
| [[SW480 (line)]] | alt | 826 | 0 | 17 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -25.7) |
| [[COLO 205 (line)]] | alt | 374 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -22.1) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.198× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 945 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -19.4) |
| [[A-172 (line)]] | wt | 162 | 7 (6 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.28× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.390× (z -10.4) |
| [[SW 900 (line)]] | alt | 405 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 514 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 541 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -20.6) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 418 | 0 | 10 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.266× (z -12.9) |
| [[Hs 766T (line)]] | wt | 354 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.9) |
| [[HS-578T (line)]] | alt | 436 | 7 (2 ⚠) | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 3.11× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.371× (z -9.1) |
| [[PANC-1 (line)]] | alt | 169 | 1 (1 ⚠) | 7 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.58× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.366× (z -10.9) |
| [[SW1417 (line)]] | alt | 748 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -19.3) |
| [[AsPC-1 (line)]] | alt | 530 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -18.1) |
| [[J82 (line)]] | alt | 305 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 234 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -18.1) |
| [[SNU-423 (line)]] | alt | 381 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -14.8) |
| [[A498 (line)]] | wt | 233 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -19.4) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.290× (z -11.8) |
| [[C32 (line)]] | wt | 279 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 178 | 0 | 5 | — | [[Ixazomib citrate (drug)]] 5 µM 0.313× (z -11.6) |
| [[HT-29 (line)]] | alt | 192 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.4) ⚠ cell-cycle shift, explains ~76% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 488 | 2 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.98× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 5 µM 2.75× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -12.0) |
| [[AN3 CA (line)]] | alt | 304 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.198× (z -12.1) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 283 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -10.0) |
| [[HOP62 (line)]] | alt | 204 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.4) ⚠ cell-cycle shift, explains ~76% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +15.7) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 3.49× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 253 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.2) |
| [[A549 (line)]] | wt | 162 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.0) |
| [[H4 (line)]] | wt | 173 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.219× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 230 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -11.8) |
| [[NCI-H661 (line)]] | alt | 375 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -9.9) |
| [[SW 1271 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0620× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 68.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 42.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 56.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 37.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 64.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 434 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK6]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TGFBR2]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[IKBKE]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[ARHGAP24]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TCF7L2]] | +0.54 | +0.44 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_NOTCH_SIGNALING |
| [[MAP3K1]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TANK]] | +0.52 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[DPYD]] | +0.52 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[RBMS3]] | +0.51 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[SLFN12]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[HES1]] | +0.51 | +0.41 / +0.52 | both halves | 4e-05 | pathway: HALLMARK_NOTCH_SIGNALING; STRING 734 |
| [[ZNF608]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCC1]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[XPOT]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[TPD52L2]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RAB6A]] | -0.50 | -0.39 / -0.49 | both halves | 6e-05 | pathway: Pre-NOTCH Expression and Processing |
| [[MAP4]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SESN2]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[SVIL-AS1-1]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[HOMER2]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ISCA1]] | -0.48 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ZFYVE21]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[NRBP1]] | -0.47 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[SARS1]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA1]] | B | ITGA1 activity raises MAML2's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.73× lower at baseline in the lines without ITGA1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[EFNB2]] | B | EFNB2 activity raises MAML2's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.30× lower at baseline in the lines without EFNB2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[BMP4]] | B | BMP4 activity raises MAML2's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without BMP4 | 0.019 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[PPARG]] | B | PPARG activity raises MAML2's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without PPARG | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[SLFN12]] | B | SLFN12 activity raises MAML2's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without SLFN12 | 0.024 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[TLR4]] | B | TLR4 activity raises MAML2's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 2.43× lower at baseline in the lines without TLR4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP |
| [[EFNB2]] | B | EFNB2 activity strengthens MAML2's drug response | lines that do not express EFNB2 (10) vs lines expressing it (31) | the lines without EFNB2 respond 0.78× as strongly (z diff +1.65); strongest at Panobinostat 0.5 µM: 0.48x vs 0.31x (z diff +3.4) | 0.047 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141; target measured in part of the lines; artifact flags |
| [[ZNF608]] | B | ZNF608 activity raises MAML2's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without ZNF608 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |
| [[GJB1]] | B | GJB1 activity raises MAML2's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.53× lower at baseline in the lines without GJB1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[RASSF5]] | B | RASSF5 activity raises MAML2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 3.45× lower at baseline in the lines without RASSF5 | 0.098 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[PLD1]] | C | PLD1 activity raises MAML2's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 4.45× lower at baseline in the lines without PLD1 | 0.016 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFBR2]] | B | MAML2 activity raises TGFBR2's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 3.78× lower at baseline in the lines without MAML2 | 0.008 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[TCF7L2]] | B | MAML2 activity raises TCF7L2's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without MAML2 | 0.017 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[PPARG]] | B | MAML2 activity raises PPARG's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 4.10× lower at baseline in the lines without MAML2 | 0.018 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[LINC00511]] | B | MAML2 activity raises LINC00511's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 4.51× lower at baseline in the lines without MAML2 | 0.032 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[MET]] | B | MAML2 activity raises MET's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 3.20× lower at baseline in the lines without MAML2 | 0.032 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | B | MAML2 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 0.41× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[ITGA1]] | B | MAML2 activity raises ITGA1's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 4.58× lower at baseline in the lines without MAML2 | 0.039 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[PPP3CA]] | B | MAML2 activity raises PPP3CA's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without MAML2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[IKBKE]] | B | MAML2 activity raises IKBKE's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 2.40× lower at baseline in the lines without MAML2 | 0.068 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| cells under [[Riluzole hydrochloride (drug)]] 5 µM | B | MAML2 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 0.88× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| cells under [[APTO-253 (drug)]] 0.05 µM | B | MAML2 activity lowers the cells' numbers under APTO-253 0.05 µM (makes them more sensitive) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 1.24× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| cells under [[Rimonabant (drug)]] 5 µM | B | MAML2 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 1.13× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.187). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.7, 11.5); signed map (15.5, 38.4). **Vector** length 131, 51.5% of its response variance represented; |z| ≥ 3 in 1,839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.1 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +6.2 | -2.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.9 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.5 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -7.9 | -8.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -6.7 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -6.6 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -6.5 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -10.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -6.4 | -6.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | mastermind like transcriptional coactivator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:95,976,598-96,343,195 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1819, MAM3 |
| Gene groups (HGNC) | Mastermind like transcriptional coactivator family |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 28 pathways, smallest: NOTCH2 intracellular domain regulates transcription; RUNX3 regulates NOTCH signaling; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZL2](https://www.uniprot.org/uniprotkb/Q8IZL2) (Mastermind-like protein 2):

> Acts as a transcriptional coactivator for NOTCH proteins. Has been shown to amplify NOTCH-induced transcription of HES1. Potentiates activation by NOTCH3 and NOTCH4 more efficiently than MAML1 or MAML3.

**Summary**, from NCBI Gene [84441](https://www.ncbi.nlm.nih.gov/gene/84441):

> The protein encoded by this gene is a member of the Mastermind-like family of proteins. All family members are proline and glutamine-rich, and contain a conserved basic domain that binds the ankyrin repeat domain of the intracellular domain of the Notch receptors (ICN1-4) in their N-terminus, and a transcriptional activation domain in their C-terminus. This protein binds to an extended groove that is formed by the interaction of CBF1, Suppressor of Hairless, LAG-1 (CSL) with ICN, and positively …

**Accessions** — [HGNC:16259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16259) · Entrez [84441](https://www.ncbi.nlm.nih.gov/gene/84441) · UniProt [Q8IZL2](https://www.uniprot.org/uniprotkb/Q8IZL2) · Ensembl [ENSG00000184384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184384)

## Data

Gene col 11530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11530); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11530]; `tensor/DDL_lfc|DDL_z.npy` [11530]; `embed/gene_vectors.npy` [11530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11530 or target_col == 11530). Every well: [[MAML2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAML2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
