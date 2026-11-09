---
symbol: "THOP1"
type: "gene"
col: 10198
ensembl_id: "ENSG00000172009"
name: "thimet oligopeptidase 1"
location: "19p13.3"
module: 43
arm: "-"
pooled_cpm: 12.7
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# THOP1

*thimet oligopeptidase 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.95× (z +18.8, q 0e+00, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.55× (z +11.6, q 3e-29, up in 34 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.234×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (AsPC-1 0.0948×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAAP100]] (+0.69, fdr 7e-06), [[AP1B1]] (+0.65, fdr 7e-06), [[ARFRP1]] (+0.64, fdr 1e-05); moves opposite to [[RPS20]] (-0.65, fdr 7e-06), [[RPL39]] (-0.62, fdr 7e-06), [[MKRN1]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 20 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.95×** | +18.8 | 0e+00 | 39/46 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **3.50×** | +15.5 | 0e+00 | 35/37 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.25×** | +14.0 | 1e-42 | 41/46 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **3.04×** | +13.8 | 5e-41 | 45/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.81×** | +12.3 | 6e-33 | 20/20 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.55×** | +11.6 | 3e-29 | 34/45 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.33×** | +10.5 | 6e-24 | 42/47 (SW480, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.40×** | +10.5 | 6e-24 | 41/47 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.27×** | +9.4 | 3e-19 | 20/27 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.08×** | +9.1 | 7e-18 | 41/47 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.84×** | +7.5 | 2e-12 | 29/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.73×** | +6.8 | 7e-10 | 28/45 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +5.6 | 9e-07 | 23/47 (SW480, BT-474, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.60×** | +5.6 | 1e-06 | 23/40 (A-427, A-172, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.54×** | +5.3 | 4e-06 | 22/39 (SNU-423, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +4.5 | 3e-04 | 15/47 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **2.00×** | +4.4 | 4e-04 | 14/40 (SW480, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.99×** | +4.3 | 4e-04 | 11/45 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.93×** | +4.1 | 1e-03 | 11/44 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.001 | 15/47 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.87×** | +3.9 | 0.002 | 13/45 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.82×** | +3.8 | 0.004 | 12/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.015 | 8/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.021 | 6/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.029 | 6/43 (NCI-H460, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.047 | 7/48 (SW1417, SNU-1, …) | all doses, stronger at high dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.049 | 3/46 (PANC-1, HCT15, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10198.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.234×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (AsPC-1 0.0948×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.746× | -3.7 | 0.14 | 13/46 (RPMI-7951, LS 180, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.583× | -3.4 | 0.19 | 8/46 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.779× | -3.0 | 0.46 | 8/47 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.71 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.8 | 12 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +20.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 10.8 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +19.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.43× (z +14.2) | — |
| [[SW1417 (line)]] | alt | 15.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +20.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.77× (z +12.7) | — |
| [[A-172 (line)]] | wt | 24.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 5.15 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 26.2× (z +17.3) ⚠ cell-cycle shift, explains ~27% of this change | [[Bendamustine (drug)]] 5 µM 0.0948× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 11.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[KATO III (line)]] | alt | 8.88 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +11.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 13.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 22.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 11.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +12.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 9.39 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 5.33 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.0× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +12.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 9.19 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 5.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 8.81 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +11.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +16.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAP100]] | +0.69 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[AP1B1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ARFRP1]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 | STRING 420 |
| [[SLC35A4]] | +0.63 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[DNMT1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ZNF512B]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ARHGDIA]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[PFAS]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NUP188]] | +0.57 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[APEH]] | +0.56 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[RHOT2]] | +0.56 | +0.46 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS20]] | -0.65 | -0.69 / -0.67 | both halves | 7e-06 |  |
| [[RPL39]] | -0.62 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[MKRN1]] | -0.60 | -0.57 / -0.57 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PCMTD1]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[FTL]] | -0.58 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RPL30]] ⚠ | -0.58 | -0.55 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL27A]] | -0.58 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[ZNF394]] | -0.57 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[RPS4X]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[RPS12]] | -0.56 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[RPL13A]] | -0.56 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[RPL12]] | -0.56 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[RPS11]] | -0.55 | -0.61 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **-** arm (projection on the module's main direction -0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.1, -32.5); signed map (-2.2, -35.5). **Vector** length 75.3, 15.5% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.3 | +14.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.6 | +18.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +4.3 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +4.1 | +12.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +4.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.9 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | thimet oligopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,785,503-2,815,807 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M3 metallopeptidase family |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P52888](https://www.uniprot.org/uniprotkb/P52888) (Thimet oligopeptidase):

> Involved in the metabolism of neuropeptides under 20 amino acid residues long. Involved in cytoplasmic peptide degradation. Able to degrade the amyloid-beta precursor protein and generate amyloidogenic fragments. Also acts as a regulator of cannabinoid signaling pathway by mediating degradation of hemopressin, an antagonist peptide of the cannabinoid receptor CNR1 (By similarity).

**Summary**, from NCBI Gene [7064](https://www.ncbi.nlm.nih.gov/gene/7064):

> The protein encoded by this gene is a kininase that uses zinc as a cofactor. The encoded oligopeptidase cleaves cytosolic peptides, making them unavailable for display on antigen-presenting cells. This protein also cleaves neuropeptides under 20 aa in length and can degrade beta-amyloid precursor protein to amyloidogenic peptides. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:11793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11793) · Entrez [7064](https://www.ncbi.nlm.nih.gov/gene/7064) · UniProt [P52888](https://www.uniprot.org/uniprotkb/P52888) · Ensembl [ENSG00000172009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172009)

## Data

Gene col 10198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10198); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10198]; `tensor/DDL_lfc|DDL_z.npy` [10198]; `embed/gene_vectors.npy` [10198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10198 or target_col == 10198). Every well: [[THOP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THOP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
