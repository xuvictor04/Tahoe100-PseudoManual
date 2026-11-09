---
symbol: "OLA1"
type: "gene"
col: 6173
ensembl_id: "ENSG00000138430"
name: "Obg like ATPase 1"
location: "2q31.1"
module: 188
arm: "+"
pooled_cpm: 224.05
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# OLA1

*Obg like ATPase 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +16.5, q 0e+00, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.346×, SNU-1 0.460×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 1271 0.0628×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.604×; ⚠ cell-cycle shift, explains ~61% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.594×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAR1]] (+0.67, fdr 7e-06), [[PSMD14]] (+0.65, fdr 9e-06), [[OTUD6B]] (+0.61, fdr 1e-05); moves opposite to [[THAP1]] (-0.60, fdr 1e-05), [[BOD1L1]] (-0.59, fdr 1e-05), [[RXRB]] (-0.56, fdr 1e-05).
> It is in [[Module 188]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +16.5 | 0e+00 | 40/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +12.3 | 3e-32 | 47/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +10.4 | 4e-23 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.68×** | +10.4 | 4e-23 | 45/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.61×** | +10.1 | 7e-22 | 46/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +10.0 | 2e-21 | 44/48 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.66×** | +9.8 | 6e-21 | 42/48 (RKO, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.57×** | +9.1 | 1e-17 | 44/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +9.0 | 1e-17 | 43/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +8.6 | 4e-16 | 34/38 (SW480, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +8.4 | 3e-15 | 37/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +8.3 | 5e-15 | 43/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.51×** | +8.3 | 5e-15 | 34/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +8.0 | 5e-14 | 40/50 (A-427, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +7.8 | 3e-13 | 38/48 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +7.2 | 2e-11 | 38/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +7.0 | 1e-10 | 38/48 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +5.3 | 3e-06 | 36/49 (MIA PaCa-2, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.63×** | +5.2 | 6e-06 | 34/48 (HT-29, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.61×** | +5.0 | 1e-05 | 38/48 (HT-29, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 4e-05 | 37/48 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.56×** | +4.7 | 5e-05 | 35/48 (HT-29, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.50×** | +4.2 | 4e-04 | 30/48 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6173.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.346×, SNU-1 0.460×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 1271 0.0628×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.604×; ⚠ cell-cycle shift, explains ~61% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.833× | -3.7 | 0.10 | 19/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.839× | -3.6 | 0.10 | 18/48 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.793× | -3.4 | 0.12 | 21/48 (NCI-H661, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.12 | 20/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.12 | 14/48 (KATO III, SW480, …) | two highest doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.857× | -3.1 | 0.12 | 17/48 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.851× | -3.1 | 0.12 | 17/49 (AsPC-1, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.893× | -3.1 | 0.12 | 8/49 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.862× | -3.0 | 0.15 | 17/47 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 212 | 15 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +21.8) | — |
| [[LoVo (line)]] | wt | 243 | 14 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +18.8) | — |
| [[HT-29 (line)]] | alt | 131 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +20.0) | — |
| [[NCI-H1573 (line)]] | alt | 129 | 10 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.55× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 282 | 10 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.4) | — |
| [[SW480 (line)]] | alt | 288 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +12.5) | — |
| [[KATO III (line)]] | alt | 140 | 6 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +18.6) | [[Sunitinib (drug)]] 5 µM 0.498× (z -8.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 254 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.53× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 81.2 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 223 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.17× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 360 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.3) | — |
| [[RKO (line)]] | wt | 380 | 3 (2 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -11.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-427 (line)]] | wt | 174 | 3 (3 ⚠) | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +14.2) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.346× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 197 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 299 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.5) | — |
| [[H4 (line)]] | wt | 167 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 214 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 309 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.438× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 182 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 160 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.95× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +11.1) | — |
| [[A-172 (line)]] | wt | 190 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.8) | — |
| [[HCT15 (line)]] | alt | 327 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 124 | 3 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.56× (z +9.9) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 133 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +8.9) | — |
| [[A498 (line)]] | wt | 244 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +15.5) | — |
| [[C32 (line)]] | wt | 208 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 186 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 194 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.0) | — |
| [[SK-MEL-2 (line)]] | alt | 198 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 342 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.460× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.594× (z -9.1) |
| [[SW1417 (line)]] | alt | 310 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.21× (z +9.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A549 (line)]] | wt | 259 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 207 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.8) | — |
| [[J82 (line)]] | alt | 287 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.3) | — |
| [[SW 1271 (line)]] | alt | 235 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0628× (z -17.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 180 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.3) | — |
| [[SW48 (line)]] | wt | 247 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 322 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 278 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 164 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 240 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAR1]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[PSMD14]] | +0.65 | +0.73 / +0.57 | both halves | 9e-06 | STRING 488 |
| [[OTUD6B]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SERGEF]] | +0.60 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[DHX15]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[HPRT1]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[BOLA3]] | +0.58 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[SNRPA1]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[KDM1A]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[IPO7]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[NME1]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MFSD14B]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP1]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[BOD1L1]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[RXRB]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SIRT1]] | -0.56 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MFAP1]] | -0.55 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[RFX1]] | -0.53 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[TOPORS]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[EP300]] | -0.53 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[PNRC1]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SLU7]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ZNF24]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[OTUD5]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.9, -13.3); signed map (-28.3, -29.9). **Vector** length 97.2, 38.8% of its response variance represented; |z| ≥ 3 in 1,558 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +8.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.9 | +9.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.9 | +5.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +4.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.7 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.5 | +10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.2 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.9 | -1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | Obg like ATPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:174,072,447-174,248,599 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTD004; previously GTPBP9 |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTK5](https://www.uniprot.org/uniprotkb/Q9NTK5) (Obg-like ATPase 1):

> Hydrolyzes ATP, and can also hydrolyze GTP with lower efficiency. Has lower affinity for GTP.

**Summary**, from NCBI Gene [29789](https://www.ncbi.nlm.nih.gov/gene/29789):

> This gene encodes a member of the GTPase protein family. The encoded protein interacts with breast cancer-associated gene 1 (BRCA1) and BRCA1-associated RING domain protein (BARD1), and is involved in centrosome regulation. Overexpression of this gene has been observed in multiple types of cancer and may be associated with poor survival. Pseudogenes of this gene have been defined on chromosomes 17 and 22. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:28833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28833) · Entrez [29789](https://www.ncbi.nlm.nih.gov/gene/29789) · UniProt [Q9NTK5](https://www.uniprot.org/uniprotkb/Q9NTK5) · Ensembl [ENSG00000138430](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138430)

## Data

Gene col 6173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6173); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6173]; `tensor/DDL_lfc|DDL_z.npy` [6173]; `embed/gene_vectors.npy` [6173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6173 or target_col == 6173). Every well: [[OLA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OLA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
