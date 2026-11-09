---
symbol: "ZNF28"
type: "gene"
col: 12611
ensembl_id: "ENSG00000198538"
name: "zinc finger protein 28"
location: "19q13.41"
module: 203
arm: "+"
pooled_cpm: 19.5
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/203"]
generated_by: "tahoemap"
---

# ZNF28

*zinc finger protein 28* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.22× (z +17.7, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.652× (z -9.6, q 5e-19, down in 24 of 36 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (PANC-1 0.246×, AsPC-1 0.149×, SW480 0.369×, NCI-H2347 0.343×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.148×, PANC-1 0.406×, C-33 A 0.176×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.136×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.383×); [[Vitamin K4 (drug)]] 0.5 µM in 1 line (AN3 CA 0.134×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF468]] (+0.70, fdr 7e-06, ⚠ same locus), [[ZNF600]] (+0.68, fdr 7e-06, ⚠ same locus), [[ZNF813]] (+0.68, fdr 7e-06), [[ZSCAN32]] (+0.63, fdr 1e-05), [[ZNF761]] (+0.61, fdr 1e-05); moves opposite to [[SKA2]] (-0.45, fdr 5e-04), [[PIGK]] (-0.45, fdr 1e-04), [[DUT]] (-0.44, fdr 1e-04).
> It is in [[Module 203]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ZNF525]] → it (grade B ⚠); 12 go from it, the strongest it → [[CTU1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +17.7 | 0e+00 | 37/42 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +17.2 | 0e+00 | 38/42 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +14.3 | 4e-44 | 35/38 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +13.3 | 2e-38 | 33/42 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +10.7 | 2e-24 | 27/41 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +10.6 | 4e-24 | 23/41 (COLO 205, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +7.4 | 9e-12 | 20/42 (SW480, SW1417, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +7.4 | 9e-12 | 20/41 (LoVo, J82, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +7.2 | 5e-11 | 17/41 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +6.8 | 7e-10 | 21/41 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +6.6 | 2e-09 | 16/41 (LS 180, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +6.1 | 4e-08 | 16/42 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +5.7 | 5e-07 | 15/42 (SW 900, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.7 | 6e-07 | 18/41 (LoVo, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.28×** | +5.5 | 1e-06 | 18/42 (RPMI-7951, J82, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.2 | 7e-06 | 20/41 (J82, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.014 | 5/39 (SNU-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.4 | 0.022 | 8/41 (LoVo, NCI-H460, …) | top dose only | position effect removed |
| [[Fusidic acid (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.024 | 3/42 (HT-29, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.025 | 2/41 (J82, LoVo) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.039 | 8/41 (SW480, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12611.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (PANC-1 0.246×, AsPC-1 0.149×, SW480 0.369×, NCI-H2347 0.343×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.148×, PANC-1 0.406×, C-33 A 0.176×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.136×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.383×); [[Vitamin K4 (drug)]] 0.5 µM in 1 line (AN3 CA 0.134×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.652×** | -9.6 | 5e-19 | 24/36 (SK-MEL-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -7.4 | 3e-11 | 16/27 (PANC-1, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Malotilate (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.18 | 6/42 (hTERT-HPNE, RKO, …) | inconsistent across doses | position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | 0.869× | -3.2 | 0.18 | 3/42 (NCI-H460, HOP62, …) | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | 0.860× | -3.2 | 0.18 | 11/40 (COLO 205, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 36.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.91× (z +9.5) | — |
| [[SW480 (line)]] | alt | 29.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.11× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.23× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 18.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.253× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[LS 180 (line)]] | wt | 24.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -16.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 34.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.9) |
| [[A-427 (line)]] | wt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -18.6) |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.5 µM 0.134× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -12.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 37.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0784× (z -10.4) ⚠ transcription drop; unreliable plate only |
| [[KATO III (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -10.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF468]] | +0.70 | +0.72 / +0.72 | both halves | 7e-06 | same gene group; STRING 785; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF600]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 | same gene group; ⚠ same locus (10.6 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF813]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZSCAN32]] | +0.63 | +0.57 / +0.68 | both halves | 1e-05 | same gene group |
| [[ZNF761]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF473]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 | same gene group |
| [[ZNF845]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 | same gene group |
| [[ZNF701]] | +0.58 | +0.67 / +0.54 | both halves | 1e-05 | same gene group; STRING 517 |
| [[ZNF765]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 | same gene group; pathway: Epigenetic regulation of gene expression |
| [[ZNF317]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 | same gene group; pathway: Epigenetic regulation of gene expression |
| [[ZNF611]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 | same gene group |
| [[ZNF525]] | +0.55 | +0.53 / +0.59 | both halves | 1e-05 | same gene group; STRING 464 |
| [[ZNF669]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 | same gene group; pathway: Epigenetic regulation of gene expression |
| [[ZNF737]] | +0.53 | +0.37 / +0.59 | both halves | 8e-05 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKA2]] | -0.45 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[PIGK]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[DUT]] | -0.44 | -0.37 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF525]] | B | ZNF525 activity raises ZNF28's level | lines that do not express ZNF525 (10) vs lines expressing it (40) | 2.55× lower at baseline in the lines without ZNF525 | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF331, ZNF577, ZNF83 |
| [[ZNF790-AS1]] | B | ZNF790-AS1 activity raises ZNF28's level | lines that do not express ZNF790-AS1 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without ZNF790-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF880, ZNF829, ZNF354C |
| [[ZNF600]] | C | ZNF600 activity raises ZNF28's level | lines that do not express ZNF600 (9) vs lines expressing it (41) | 4.40× lower at baseline in the lines without ZNF600 | 2e-05 | ⚠ within organs, on part of the lines; also absent: ZNF320, ZNF28, ZNF468; co-absent with the target |
| [[ZNF320]] | C | ZNF320 activity raises ZNF28's level | lines that do not express ZNF320 (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without ZNF320 | 7e-05 | ⚠ within organs, on part of the lines; also absent: ZNF600, LYPD5, ZNF701; co-absent with the target |
| [[ZNF468]] | C | ZNF468 activity raises ZNF28's level | lines that do not express ZNF468 (5) vs lines expressing it (45) | 6.68× lower at baseline in the lines without ZNF468 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF701, ZNF28, ZNF888; co-absent with the target |
| [[ZNF701]], [[ZNF808]] | C | ZNF701, ZNF808 activity raises ZNF28's level | lines that do not express ZNF701, ZNF808 (6) vs lines expressing them (44) | 4.60× lower at baseline in the lines without ZNF701, ZNF808 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF28, ZNF888; co-absent with the target; co-absent genes |
| [[ZNF761]] | C | ZNF761 activity raises ZNF28's level | lines that do not express ZNF761 (3) vs lines expressing it (47) | 6.20× lower at baseline in the lines without ZNF761 | 9e-04 | ⚠ few lines (3 vs 47); across organs; also absent: ZNF468, ZNF845, FAM102A; co-absent with the target |
| [[ZNF611]] | C | ZNF611 activity raises ZNF28's level | lines that do not express ZNF611 (3) vs lines expressing it (47) | 6.07× lower at baseline in the lines without ZNF611 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF468, ZNF845, ZNF14; co-absent with the target; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTU1]] | B | ZNF28 activity lowers CTU1's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 1.61× higher at baseline in the lines without ZNF28 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888 |
| [[ZNF765]] | B | ZNF28 activity raises ZNF765's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without ZNF28 | 0.031 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888 |
| [[ZNF525]] | B | ZNF28 activity raises ZNF525's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 3.43× lower at baseline in the lines without ZNF28 | 0.042 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888 |
| [[ZNF790-AS1]] | B | ZNF28 activity raises ZNF790-AS1's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without ZNF28 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888 |
| [[ZNF468]] | C | ZNF28 activity raises ZNF468's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 4.34× lower at baseline in the lines without ZNF28 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888; co-absent with the target |
| [[ZNF320]] | C | ZNF28 activity raises ZNF320's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 5.71× lower at baseline in the lines without ZNF28 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888; co-absent with the target |
| [[ZNF600]] | C | ZNF28 activity raises ZNF600's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 5.85× lower at baseline in the lines without ZNF28 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888; co-absent with the target |
| [[ZNF701]] | C | ZNF28 activity raises ZNF701's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 5.04× lower at baseline in the lines without ZNF28 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888; co-absent with the target |
| [[ZNF808]] | C | ZNF28 activity raises ZNF808's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 4.79× lower at baseline in the lines without ZNF28 | 0.001 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888; co-absent with the target |
| [[ZNF761]] | C | ZNF28 activity raises ZNF761's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 3.38× lower at baseline in the lines without ZNF28 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888; co-absent with the target |
| [[ZNF845]] | C | ZNF28 activity raises ZNF845's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 3.07× lower at baseline in the lines without ZNF28 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888; co-absent with the target |
| [[ZNF611]] | C | ZNF28 activity raises ZNF611's level | lines that do not express ZNF28 (6) vs lines expressing it (44) | 3.43× lower at baseline in the lines without ZNF28 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF701, ZNF888; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 203]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-51.3, -3.6); signed map (-7.6, -14.2). **Vector** length 66.8, 10.7% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.4 | +13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +14.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +7.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +2.9 | +4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.8 | +5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +3.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | -9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | +0.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:52,797,408-52,857,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX24, DKFZp781D0275 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Reactome | 3 pathways, smallest: Regulation of endogenous retroelements by KRAB-ZFP proteins; Regulation of endogenous retroelements; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P17035](https://www.uniprot.org/uniprotkb/P17035) (Zinc finger protein 28):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7576](https://www.ncbi.nlm.nih.gov/gene/7576):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13073) · Entrez [7576](https://www.ncbi.nlm.nih.gov/gene/7576) · UniProt [P17035](https://www.uniprot.org/uniprotkb/P17035) · Ensembl [ENSG00000198538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198538)

## Data

Gene col 12611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12611); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12611]; `tensor/DDL_lfc|DDL_z.npy` [12611]; `embed/gene_vectors.npy` [12611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12611 or target_col == 12611). Every well: [[ZNF28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
