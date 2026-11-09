---
symbol: "ULK1"
type: "gene"
col: 10798
ensembl_id: "ENSG00000177169"
name: "unc-51 like autophagy activating kinase 1"
location: "12q24.33"
module: 145
arm: "+"
pooled_cpm: 52.77
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# ULK1

*unc-51 like autophagy activating kinase 1* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.31× (z +4.4, q 0.005, up in 28 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 3.10×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.361× (z -12.1, q 1e-30, down in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.506× (z -8.0, q 3e-13, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BSDC1]] (+0.75, fdr 7e-06), [[FBXL20]] (+0.73, fdr 7e-06), [[RAB40C]] (+0.72, fdr 7e-06); moves opposite to [[SF3B3]] (-0.72, fdr 7e-06), [[ABCE1]] (-0.70, fdr 7e-06), [[UTP20]] (-0.68, fdr 7e-06).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10798.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 3.10×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +4.4 | 0.005 | 28/49 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.3 | 0.005 | 26/47 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.3 | 0.16 | 22/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.30× | +3.1 | 0.16 | 24/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.54× | +3.1 | 0.16 | 20/48 (BT-474, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.53× | +3.1 | 0.16 | 20/49 (HT-29, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.30× | +3.1 | 0.16 | 19/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.52× | +3.1 | 0.16 | 17/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10798.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.361×** | -12.1 | 1e-30 | 44/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.506×** | -8.0 | 3e-13 | 39/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.274×** | -7.4 | 2e-11 | 43/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.657×** | -6.9 | 7e-10 | 33/48 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.555×** | -6.7 | 3e-09 | 37/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.551×** | -6.4 | 1e-08 | 37/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.566×** | -6.2 | 6e-08 | 28/46 (NCI-H23, SW48, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.356×** | -5.9 | 2e-07 | 38/48 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.590×** | -5.8 | 5e-07 | 28/42 (SK-MEL-2, NCI-H460, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.371×** | -5.7 | 7e-07 | 32/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.608×** | -5.6 | 8e-07 | 26/39 (HT-29, HCT15, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -5.3 | 5e-06 | 36/49 (HT-29, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.399×** | -5.3 | 6e-06 | 37/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.680×** | -4.3 | 7e-04 | 28/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.482×** | -4.2 | 0.001 | 27/47 (H4, A498, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.793×** | -3.8 | 0.006 | 27/48 (NCI-H460, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -3.5 | 0.015 | 23/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.546×** | -3.5 | 0.016 | 23/48 (NCI-H2347, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.624×** | -3.4 | 0.017 | 23/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 124 | 0 | 15 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -12.9) ⚠ unreliable plate only · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.350× (z -10.3) |
| [[HT-29 (line)]] | alt | 85.6 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -13.2) |
| [[A-172 (line)]] | wt | 145 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -19.0) |
| [[AsPC-1 (line)]] | alt | 75.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.1) |
| [[PANC-1 (line)]] | alt | 72.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 87.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.7) |
| [[SNU-423 (line)]] | alt | 58.0 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.264× (z -11.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.0) |
| [[A549 (line)]] | wt | 51.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HCT15 (line)]] | alt | 68.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 71.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -10.6) |
| [[SW48 (line)]] | wt | 34.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 33.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.335× (z -8.5) |
| [[A-427 (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -16.2) |
| [[AN3 CA (line)]] | alt | 52.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.137× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 43.6 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.10× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 56.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.120× (z -8.6) |
| [[H4 (line)]] | wt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.205× (z -11.9) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -10.3) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.311× (z -8.9) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.202× (z -10.1) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.268× (z -8.7) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -10.2) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.298× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.250× (z -13.8) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -8.6) |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.282× (z -8.5) |
| [[A498 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BSDC1]] | +0.75 | +0.65 / +0.83 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PINK1]] | +0.72 | +0.56 / +0.78 | both halves | 1e-05 | pathway: Autophagy; STRING 573 |
| [[SLC25A29]] | +0.72 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[MXD4]] | +0.71 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[MACO1]] | +0.70 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.70 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TULP3]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PHF1]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B3]] | -0.72 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.70 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[UTP20]] | -0.68 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[GUF1]] | -0.67 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[ATIC]] | -0.67 | -0.63 / -0.72 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.65 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[NOL11]] | -0.65 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.64 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[PUS7L]] | -0.64 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[MAK16]] | -0.63 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.2, -42.6); signed map (-22.2, 10.8). **Vector** length 142, 43.9% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.3 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.8 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.6 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.5 | -12.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.9 | -7.4 |
|  | [[EX229 (drug)]] 5 µM |  | -6.7 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.4 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.2 | -5.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | unc-51 like autophagy activating kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:131,894,622-131,923,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATG1, ATG1A |
| Gene groups (HGNC) | Autophagy related; Unc-51 like kinase family |
| Reactome | 13 pathways, smallest: Receptor Mediated Mitophagy; Mitophagy; TBC/RABGAPs |
| Matched by | ensembl_id |

**Function**, from UniProt [O75385](https://www.uniprot.org/uniprotkb/O75385) (Serine/threonine-protein kinase ULK1):

> Serine/threonine-protein kinase involved in autophagy in response to starvation. Acts upstream of phosphatidylinositol 3-kinase PIK3C3 to regulate the formation of autophagophores, the precursors of autophagosomes. Part of regulatory feedback loops in autophagy: acts both as a downstream effector and negative regulator of mammalian target of rapamycin complex 1 (mTORC1) via interaction with RPTOR. Activated via phosphorylation by AMPK and also acts as a regulator of AMPK by mediating …

**Summary**, from NCBI Gene [8408](https://www.ncbi.nlm.nih.gov/gene/8408):

> Enables identical protein binding activity; protein serine/threonine kinase activity; and small GTPase binding activity. Involved in several processes, including protein phosphorylation; regulation of autophagy; and regulation of protein lipidation. Located in bounding membrane of organelle; cytosol; and phagophore assembly site membrane. Part of Atg1/ULK1 kinase complex. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12558](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12558) · Entrez [8408](https://www.ncbi.nlm.nih.gov/gene/8408) · UniProt [O75385](https://www.uniprot.org/uniprotkb/O75385) · Ensembl [ENSG00000177169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177169)

## Data

Gene col 10798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10798); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10798]; `tensor/DDL_lfc|DDL_z.npy` [10798]; `embed/gene_vectors.npy` [10798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10798 or target_col == 10798). Every well: [[ULK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ULK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
