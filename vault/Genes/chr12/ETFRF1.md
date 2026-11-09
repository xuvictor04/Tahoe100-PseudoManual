---
symbol: "ETFRF1"
type: "gene"
col: 13003
ensembl_id: "ENSG00000205707"
name: "electron transfer flavoprotein regulatory factor 1"
location: "12p12.1"
module: 68
arm: "+"
pooled_cpm: 15.31
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# ETFRF1

*electron transfer flavoprotein regulatory factor 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +18.2, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.636× (z -7.4, q 8e-11, down in 28 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.722× (z -5.3, q 3e-05, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLN5]] (+0.71, fdr 7e-06), [[FAM200B]] (+0.70, fdr 7e-06), [[HHLA3]] (+0.69, fdr 7e-06); moves opposite to [[PRIM2]] (-0.67, fdr 1e-05), [[MAD1L1]] (-0.63, fdr 2e-05), [[GNB1L]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +18.2 | 0e+00 | 40/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +11.3 | 4e-27 | 28/41 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +10.9 | 3e-25 | 36/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +10.1 | 8e-22 | 34/46 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +10.0 | 2e-21 | 20/27 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +9.5 | 2e-19 | 32/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +9.5 | 3e-19 | 28/35 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +9.4 | 3e-19 | 34/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +8.5 | 9e-16 | 28/48 (SW480, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +8.5 | 9e-16 | 24/31 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +8.2 | 1e-14 | 33/47 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +8.2 | 1e-14 | 28/47 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.5 | 2e-06 | 21/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.2 | 1e-05 | 22/46 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 3e-04 | 16/46 (SW 900, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.3 | 7e-04 | 12/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 14/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.005 | 13/48 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.005 | 8/48 (SW480, NCI-H1792, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13003.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.636×** | -7.4 | 8e-11 | 28/47 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -5.3 | 3e-05 | 20/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.804×** | -3.6 | 0.043 | 13/47 (COLO 205, H4, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.651×** | -3.6 | 0.043 | 13/44 (HCT15, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.6 | 0.043 | 5/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | 0.682× | -3.2 | 0.14 | 9/45 (SHP-77, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 17.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 20.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +16.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +12.6) | — |
| [[SW480 (line)]] | alt | 42.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.2) | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +8.9) | — |
| [[J82 (line)]] | alt | 7.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +9.1) | — |
| [[LoVo (line)]] | wt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.2) | — |
| [[A-172 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN5]] | +0.71 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[FAM200B]] | +0.70 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.69 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[SEPSECS]] | +0.67 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[DNAJC27]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[PIGP]] | +0.66 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[XPA]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.65 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[LIPT1]] | +0.64 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[CUTALP]] | +0.64 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRIM2]] | -0.67 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.63 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[GNB1L]] | -0.63 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.63 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[BRI3BP]] | -0.62 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[TCOF1]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[PAQR4]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[RGS19]] | -0.59 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[EIPR1]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TBC1D24]] | -0.58 | -0.66 / -0.37 | both halves | 7e-05 |  |
| [[TMEM201]] | -0.58 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[VAV2]] | -0.58 | -0.66 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (1.8, 12.6); signed map (10.5, -20.8). **Vector** length 74.6, 13.4% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | electron transfer flavoprotein regulatory factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:25,195,216-25,209,645 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LYRM5 |
| Gene groups (HGNC) | LYR motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IPR1](https://www.uniprot.org/uniprotkb/Q6IPR1) (Electron transfer flavoprotein regulatory factor 1):

> Acts as a regulator of the electron transfer flavoprotein by promoting the removal of flavin from the ETF holoenzyme (composed of ETFA and ETFB).

**Summary**, from NCBI Gene [144363](https://www.ncbi.nlm.nih.gov/gene/144363):

> Enables enzyme inhibitor activity. Involved in negative regulation of oxidative phosphorylation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27052) · Entrez [144363](https://www.ncbi.nlm.nih.gov/gene/144363) · UniProt [Q6IPR1](https://www.uniprot.org/uniprotkb/Q6IPR1) · Ensembl [ENSG00000205707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205707)

## Data

Gene col 13003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13003); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13003]; `tensor/DDL_lfc|DDL_z.npy` [13003]; `embed/gene_vectors.npy` [13003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13003 or target_col == 13003). Every well: [[ETFRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETFRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
