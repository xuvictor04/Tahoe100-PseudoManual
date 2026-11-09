---
symbol: "H6PD"
type: "gene"
col: 546
ensembl_id: "ENSG00000049239"
name: "hexose-6-phosphate dehydrogenase/glucose 1-dehydrogenase"
location: "1p36.22"
module: 60
arm: "-"
pooled_cpm: 34.57
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 37
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# H6PD

*hexose-6-phosphate dehydrogenase/glucose 1-dehydrogenase* — 1p36.22

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 2.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (21 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.402× (z -15.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNRC2]] (+0.60, fdr 3e-05), [[LIPT1]] (+0.60, fdr 2e-05), [[PTP4A3]] (+0.56, fdr 2e-05); moves opposite to [[CACYBP]] (-0.60, fdr 1e-05), [[ATP2C1]] (-0.56, fdr 3e-05), [[MACO1]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 546.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 2.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 0.5 µM |  | 1.25× | +3.7 | 0.14 | 16/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.22× | +3.3 | 0.20 | 16/48 (KATO III, COLO 205, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.22× | +3.3 | 0.20 | 15/48 (A498, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.402×** | -15.0 | 0e+00 | 48/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.460×** | -12.8 | 4e-35 | 43/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.462×** | -12.8 | 5e-35 | 43/48 (SW480, C-33 A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.442×** | -12.7 | 5e-35 | 42/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.468×** | -12.0 | 2e-31 | 40/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.496×** | -11.6 | 6e-29 | 40/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.525×** | -10.6 | 2e-24 | 37/48 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.293×** | -10.6 | 2e-24 | 34/43 (NCI-H1573, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.343×** | -9.2 | 2e-18 | 41/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.573×** | -9.2 | 2e-18 | 38/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.582×** | -8.9 | 2e-17 | 31/47 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.574×** | -8.8 | 6e-17 | 32/48 (H4, LS 180, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -8.7 | 2e-16 | 40/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.634×** | -7.5 | 2e-12 | 36/48 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -7.4 | 6e-12 | 30/47 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -5.6 | 7e-07 | 25/47 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.658×** | -4.9 | 2e-05 | 26/48 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.841× | -4.0 | 0.001 | 15/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.777×** | -3.9 | 0.002 | 24/47 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.787×** | -3.8 | 0.003 | 23/48 (RKO, HepG2/C3A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.808×** | -3.5 | 0.008 | 16/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.868× | -3.3 | 0.016 | 17/48 (SW480, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.3 | 0 | 18 (11 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.227× (z -15.9) |
| [[PANC-1 (line)]] | alt | 49.6 | 0 | 12 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -18.0) |
| [[HOP62 (line)]] | alt | 115 | 0 | 10 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.166× (z -14.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.178× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 56.2 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -9.9) |
| [[LoVo (line)]] | wt | 35.3 | 0 | 7 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -16.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 28.6 | 1 (1 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 26.7 | 0 | 6 (4 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.108× (z -11.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.349× (z -10.1) |
| [[A-427 (line)]] | wt | 44.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 97.3 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.186× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 33.8 | 0 | 5 (5 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0345× (z -14.7) ⚠ toxic |
| [[A498 (line)]] | wt | 28.9 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.111× (z -10.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.370× (z -9.0) |
| [[A549 (line)]] | wt | 32.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.0) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -9.5) |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.178× (z -11.4) |
| [[COLO 205 (line)]] | alt | 52.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.0) |
| [[H4 (line)]] | wt | 44.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.245× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.0) |
| [[Hs 766T (line)]] | wt | 29.1 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0718× (z -9.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.262× (z -8.8) |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.238× (z -9.9) |
| [[SNU-423 (line)]] | alt | 35.8 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0375× (z -12.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.237× (z -10.7) |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -9.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.215× (z -8.5) |
| [[AN3 CA (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0832× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0544× (z -9.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -8.5) |
| [[HS-578T (line)]] | alt | 28.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.271× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0337× (z -12.3) ⚠ toxic |
| [[J82 (line)]] | alt | 23.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.225× (z -11.0) |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.224× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.363× (z -8.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0568× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -9.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[RKO (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -9.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0755× (z -17.9) |
| [[SHP-77 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.268× (z -9.3) |
| [[SW48 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0934× (z -10.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A-172 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | +0.60 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[LIPT1]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PTP4A3]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ZC3H7B]] | +0.56 | +0.55 / +0.37 | both halves | 9e-05 |  |
| [[CSF3]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[NHLRC2]] | +0.55 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[NFKB2]] | +0.54 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[KBTBD2]] | +0.54 | +0.42 / +0.37 | both halves | 7e-05 |  |
| [[DGUOK]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CHAMP1]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TKFC]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[PPP3CB]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACYBP]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ATP2C1]] | -0.56 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MACO1]] | -0.55 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[RPS6KC1]] | -0.51 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[AAK1]] | -0.51 | -0.55 / -0.27 | both halves | 3e-04 |  |
| [[GDAP2]] | -0.51 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[ANKRD39]] | -0.51 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[ZFAND2A]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TNPO3]] | -0.49 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.49 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[RELCH]] | -0.49 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[SAP130]] | -0.49 | -0.46 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **-** arm (projection on the module's main direction -0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.5, 23.6); signed map (6.3, -19.2). **Vector** length 80.0, 18.8% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.8 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.1 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | -5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.0 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +2.9 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.0 | -15.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.4 | -12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -12.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -12.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.7 | -10.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -9.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -4.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | hexose-6-phosphate dehydrogenase/glucose 1-dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:9,234,774-9,271,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H6PDH; previously GDH |
| Gene groups (HGNC) | Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95479](https://www.uniprot.org/uniprotkb/O95479) (GDH/6PGL endoplasmic bifunctional protein):

> Bifunctional enzyme localized in the lumen of the endoplasmic reticulum that catalyzes the first two steps of the oxidative branch of the pentose phosphate pathway/shunt, an alternative to glycolysis and a major source of reducing power and metabolic intermediates for biosynthetic processes (By similarity). Has a hexose-6-phosphate dehydrogenase activity, with broad substrate specificity compared to glucose-6-phosphate 1-dehydrogenase/G6PD, and catalyzes the first step of the pentose phosphate …

**Summary**, from NCBI Gene [9563](https://www.ncbi.nlm.nih.gov/gene/9563):

> There are 2 forms of glucose-6-phosphate dehydrogenase. G form is X-linked and H form, encoded by this gene, is autosomally linked. This H form shows activity with other hexose-6-phosphates, especially galactose-6-phosphate, whereas the G form is specific for glucose-6-phosphate. Both forms are present in most tissues, but H form is not found in red cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4795) · Entrez [9563](https://www.ncbi.nlm.nih.gov/gene/9563) · UniProt [O95479](https://www.uniprot.org/uniprotkb/O95479) · Ensembl [ENSG00000049239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049239)

## Data

Gene col 546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 546); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 546]; `tensor/DDL_lfc|DDL_z.npy` [546]; `embed/gene_vectors.npy` [546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 546 or target_col == 546). Every well: [[H6PD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H6PD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
