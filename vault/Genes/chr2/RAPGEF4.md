---
symbol: "RAPGEF4"
type: "gene"
col: 1662
ensembl_id: "ENSG00000091428"
name: "Rap guanine nucleotide exchange factor 4"
location: "2q31.1"
module: 26
arm: "+"
pooled_cpm: 28.72
n_lines_expressing: 45
n_dd_up: 22
n_dd_down: 21
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 7
direction_downstream: 10
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# RAPGEF4

*Rap guanine nucleotide exchange factor 4* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.08× (z +8.0, q 1e-12, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.212× (z -24.9, q 0e+00, down in 36 of 42 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02641]] (+0.65, fdr 1e-05), [[SLC26A7]] (+0.62, fdr 1e-05), [[MGAM]] (+0.61, fdr 8e-05); moves opposite to [[RFFL]] (-0.47, fdr 4e-05), [[RNF34]] (-0.46, fdr 4e-05), [[C19orf47]] (-0.45, fdr 3e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02641]] → it (grade B ⚠); 10 go from it, the strongest it → [[SYCP2L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.08×** | +8.0 | 1e-12 | 33/42 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +7.9 | 1e-12 | 29/43 (KATO III, HS-578T, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.59×** | +5.6 | 3e-06 | 29/43 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.4 | 1e-05 | 22/42 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +5.3 | 1e-05 | 22/43 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.35×** | +4.8 | 1e-04 | 18/43 (LS 180, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.5 | 6e-04 | 23/43 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.3 | 1e-03 | 20/42 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.3 | 1e-03 | 20/43 (A-172, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.003 | 19/42 (A-172, SW480, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.005 | 17/43 (NCI-H23, SHP-77, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.008 | 20/42 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.6 | 0.012 | 16/41 (A-172, SNU-423, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.026 | 12/43 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.052 | 6/43 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.72×** | +3.2 | 0.052 | 6/43 (NCI-H23, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.052 | 15/43 (NCI-H23, BT-474, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1662.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.212×** | -24.9 | 0e+00 | 36/42 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.366×** | -11.0 | 1e-25 | 33/43 (NCI-H460, A498, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.367×** | -10.9 | 1e-25 | 32/39 (COLO 205, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.416×** | -10.0 | 3e-21 | 32/40 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.615×** | -5.5 | 4e-06 | 22/40 (SW480, HEC-1-A, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.645×** | -5.0 | 5e-05 | 26/42 (HCT15, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -4.9 | 7e-05 | 22/42 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.654×** | -4.8 | 9e-05 | 19/43 (SW480, SW1417, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.659×** | -4.8 | 1e-04 | 22/43 (SW480, HCT15, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.672×** | -4.5 | 3e-04 | 19/43 (SW480, SW1417, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.771×** | -4.2 | 0.001 | 24/43 (C32, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.701×** | -4.1 | 0.002 | 22/43 (NCI-H460, C32, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **0.709×** | -3.9 | 0.004 | 19/40 (NCI-H23, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -3.6 | 0.011 | 14/43 (Hs 766T, COLO 205, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.586×** | -3.2 | 0.056 | 14/39 (HOP62, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.754×** | -3.1 | 0.068 | 9/43 (SW480, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.758×** | -2.9 | 0.096 | 16/42 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.2 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -36.9) |
| [[SW1417 (line)]] | alt | 84.6 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -21.6) |
| [[SW480 (line)]] | alt | 90.6 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 47.4 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.33× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -20.4) |
| [[HEC-1-A (line)]] | alt | 32.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.9) |
| [[A498 (line)]] | wt | 14.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -17.1) |
| [[COLO 205 (line)]] | alt | 43.3 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0266× (z -19.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.9) |
| [[A-172 (line)]] | wt | 16.6 | 1 | 2 | [[Auranofin (drug)]] 5 µM 13.3× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.4) |
| [[C32 (line)]] | wt | 76.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -17.1) |
| [[CHP-212 (line)]] | wt | 89.4 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0366× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.191× (z -10.9) |
| [[HS-578T (line)]] | alt | 26.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.140× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -16.7) |
| [[NCI-H1573 (line)]] | alt | 20.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -15.1) |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.8) |
| [[HOP62 (line)]] | alt | 25.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 23.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.218× (z -12.6) |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -13.8) |
| [[SHP-77 (line)]] | alt | 97.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 20.3 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.29× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.5) |
| [[SW48 (line)]] | wt | 26.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -9.8) |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -8.8) |
| [[H4 (line)]] | wt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -10.8) |
| [[HCT15 (line)]] | alt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.9) |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -13.1) |
| [[KATO III (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.7) |
| [[LoVo (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.1) |
| [[PANC-1 (line)]] | alt | 7.62 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -9.8) |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0974× (z -9.1) |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02641]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SLC26A7]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[MGAM]] | +0.61 | +0.37 / +0.69 | both halves | 8e-05 |  |
| [[LINC02937]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[BAALC-AS1]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[BCO2]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[LINC02762]] | +0.58 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[FRZB]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[DAB1]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CORIN]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CMYA5]] | +0.54 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[LINC01505]] | +0.54 | +0.33 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFFL]] | -0.47 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[RNF34]] | -0.46 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[C19orf47]] | -0.45 | -0.30 / -0.29 | both halves | 3e-04 |  |
| [[USP4]] | -0.45 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[MTRES1]] | -0.44 | -0.36 / -0.25 | both halves | 4e-04 |  |
| [[KDM1B]] | -0.44 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[TNIP2]] | -0.44 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[ASL]] | -0.44 | -0.42 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[RNF166]] | -0.43 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[SUGT1P4-STRA6LP]] | -0.43 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[BSN]] | -0.43 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[MTMR9]] | -0.42 | -0.37 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02641]] | B | LINC02641 activity raises RAPGEF4's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without LINC02641 | 0.001 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[MGC4859]] | B | MGC4859 activity raises RAPGEF4's level | lines that do not express MGC4859 (8) vs lines expressing it (42) | 2.71× lower at baseline in the lines without MGC4859 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC00922, LINC01811, LINC00276; maybe low, not absent |
| [[LINC02940]] | B | LINC02940 activity raises RAPGEF4's level | lines that do not express LINC02940 (10) vs lines expressing it (40) | 2.49× lower at baseline in the lines without LINC02940 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02641; maybe low, not absent |
| [[LINC01482]] | B | LINC01482 activity raises RAPGEF4's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 3.06× lower at baseline in the lines without LINC01482 | 0.078 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |
| [[DISC1]] | B | DISC1 activity raises RAPGEF4's level | lines that do not express DISC1 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without DISC1 | 0.086 | ⚠ within organs, on part of the lines; also absent: DCP1B, LINC01341, ENSG00000237356; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers RAPGEF4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[LRRIQ3]] | C | LRRIQ3 activity raises RAPGEF4's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCP2L]] | B | RAPGEF4 activity raises SYCP2L's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 3.72× lower at baseline in the lines without RAPGEF4 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[CCDC146]] | B | RAPGEF4 activity raises CCDC146's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without RAPGEF4 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[LINC02762]] | B | RAPGEF4 activity raises LINC02762's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.96× lower at baseline in the lines without RAPGEF4 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[DARS1-AS1]] | B | RAPGEF4 activity raises DARS1-AS1's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without RAPGEF4 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[TPTE2]] | B | RAPGEF4 activity raises TPTE2's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without RAPGEF4 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[MTRES1]] | B | RAPGEF4 activity raises MTRES1's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without RAPGEF4 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[LINC02641]] | B | RAPGEF4 activity raises LINC02641's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 3.57× lower at baseline in the lines without RAPGEF4 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[DAB1]] | B | RAPGEF4 activity raises DAB1's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without RAPGEF4 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[ARMCX5-GPRASP2]] | B | RAPGEF4 activity raises ARMCX5-GPRASP2's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without RAPGEF4 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[TNIP2]] | B | RAPGEF4 activity lowers TNIP2's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.42× higher at baseline in the lines without RAPGEF4 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.5, 17.4); signed map (22.2, 0.3). **Vector** length 90.7, 20.4% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.2 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -24.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.7 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.5 | -10.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Rap guanine nucleotide exchange factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:172,735,274-173,052,893 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cAMP-GEFII, CGEF2 |
| Gene groups (HGNC) | DEP domain containing |
| Reactome | 9 pathways, smallest: Rap1 signalling; Integrin signaling; Platelet Aggregation (Plug Formation) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZA2](https://www.uniprot.org/uniprotkb/Q8WZA2) (Rap guanine nucleotide exchange factor 4):

> Guanine nucleotide exchange factor (GEF) for RAP1A, RAP1B and RAP2A small GTPases that is activated by binding cAMP. Does not seem to activate RAB3A. Involved in cAMP-dependent, PKA-independent exocytosis through interaction with RIMS2 (By similarity).

**Summary**, from NCBI Gene [11069](https://www.ncbi.nlm.nih.gov/gene/11069):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in Rap protein signal transduction; regulation of neurotransmitter receptor localization to postsynaptic specialization membrane; and regulation of postsynapse organization. Predicted to act upstream of or within with a positive effect on hormone secretion. Predicted to act upstream of or within adenylate cyclase-activating G protein-coupled receptor signaling pathway; regulation of exocytosis; and secretion by cell. …

**Accessions** — [HGNC:16626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16626) · Entrez [11069](https://www.ncbi.nlm.nih.gov/gene/11069) · UniProt [Q8WZA2](https://www.uniprot.org/uniprotkb/Q8WZA2) · Ensembl [ENSG00000091428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091428)

## Data

Gene col 1662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1662); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1662]; `tensor/DDL_lfc|DDL_z.npy` [1662]; `embed/gene_vectors.npy` [1662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1662 or target_col == 1662). Every well: [[RAPGEF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPGEF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
