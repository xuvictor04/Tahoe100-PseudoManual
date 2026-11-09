---
symbol: "R3HCC1L"
type: "gene"
col: 9226
ensembl_id: "ENSG00000166024"
name: "R3H domain and coiled-coil containing 1 like"
location: "10q24.2"
module: 3
arm: "+"
pooled_cpm: 105.65
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# R3HCC1L

*R3H domain and coiled-coil containing 1 like* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.37× (z +3.8, q 0.078, up in 22 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.369× (z -23.8, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.871× (z -3.3, q 0.051, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (AsPC-1 0.0961×, A-172 0.135×, NCI-H23 0.134×, SW48 0.0989×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RPMI-7951 0.122×, SNU-423 0.214×, SNU-1 0.119×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.216×, AsPC-1 0.228×, Hs 766T 0.208×; ⚠ toxic; transcription drop); [[Neratinib (drug)]] 5 µM in 1 line (SW 1088 0.0808×); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.513×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD10]] (+0.56, fdr 7e-06), [[C8orf76]] (+0.56, fdr 1e-05), [[OXSM]] (+0.56, fdr 3e-05); moves opposite to [[SRSF6]] (-0.50, fdr 2e-05), [[SRSF10]] (-0.48, fdr 4e-05), [[CCDC180]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.078 | 22/49 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.14× | +3.1 | 0.38 | 13/47 (AN3 CA, LOX-IMVI, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.29× | +3.0 | 0.38 | 14/48 (SNU-423, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9226.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (AsPC-1 0.0961×, A-172 0.135×, NCI-H23 0.134×, SW48 0.0989×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RPMI-7951 0.122×, SNU-423 0.214×, SNU-1 0.119×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.216×, AsPC-1 0.228×, Hs 766T 0.208×; ⚠ toxic; transcription drop); [[Neratinib (drug)]] 5 µM in 1 line (SW 1088 0.0808×); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.513×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.369×** | -23.8 | 0e+00 | 46/49 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -19.8 | 0e+00 | 39/44 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.472×** | -16.5 | 0e+00 | 42/45 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -12.7 | 5e-35 | 42/47 (SNU-423, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.823×** | -6.3 | 4e-08 | 26/48 (NCI-H1792, AN3 CA, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.788×** | -5.7 | 1e-06 | 31/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.788×** | -5.4 | 4e-06 | 26/48 (NCI-H1573, COLO 205, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.818×** | -4.6 | 3e-04 | 24/47 (CFPAC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.859× | -3.6 | 0.017 | 20/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | 0.859× | -3.6 | 0.017 | 21/48 (LS 180, SW1417, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.871× | -3.3 | 0.051 | 20/48 (SNU-423, A-172, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.761×** | -3.3 | 0.051 | 16/49 (NCI-H23, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.868× | -3.2 | 0.051 | 15/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.830×** | -3.2 | 0.062 | 16/48 (RKO, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 146 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.513× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 120 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -15.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 105 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -25.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 123 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -16.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 119 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -15.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 156 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 118 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -17.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -13.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 130 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -16.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 116 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -15.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 92.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -12.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 131 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0961× (z -28.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -18.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -13.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 99.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -16.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 77.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 95.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -13.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 101 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -13.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 95.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 81.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -15.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -13.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.5) ⚠ cell-cycle shift, explains ~77% of this change |
| [[BT-474 (line)]] | alt | 75.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -18.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 89.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 88.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 92.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -24.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -13.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -22.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -17.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 88.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -17.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 86.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -18.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 92.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -17.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 81.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0808× (z -9.5) |
| [[SW 1271 (line)]] | alt | 87.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 85.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -20.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 86.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD10]] | +0.56 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[C8orf76]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[OXSM]] | +0.56 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[CNIH4]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[BMT2]] | +0.53 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[GTF2A2]] | +0.53 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[SLIRP]] | +0.53 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[TCAF2]] | +0.52 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[CCDC167]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[DENR]] | +0.51 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[IL17RA]] | +0.51 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[SEC61G]] | +0.51 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF6]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SRSF10]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CCDC180]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CLCN4]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[CYB561]] | -0.46 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[SFPQ]] | -0.45 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SCML1]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[HNRNPD]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[BTD]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[THBS1]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ILF3]] | -0.45 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[NID1]] | -0.45 | -0.48 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.371). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.2, -13.2); signed map (-43.8, 28.1). **Vector** length 84.9, 20.8% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.1 | +2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +1.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -5.7 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.6 | -16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.1 | -23.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -19.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | R3H domain and coiled-coil containing 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:98,134,624-98,244,897 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GIDRP88, PSORT; previously C10orf28 |
| Matched by | ensembl_id |

UniProt [Q7Z5L2](https://www.uniprot.org/uniprotkb/Q7Z5L2) carries no function annotation.

**Summary**, from NCBI Gene [27291](https://www.ncbi.nlm.nih.gov/gene/27291):

> Located in exon-exon junction complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23512) · Entrez [27291](https://www.ncbi.nlm.nih.gov/gene/27291) · UniProt [Q7Z5L2](https://www.uniprot.org/uniprotkb/Q7Z5L2) · Ensembl [ENSG00000166024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166024)

## Data

Gene col 9226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9226); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9226]; `tensor/DDL_lfc|DDL_z.npy` [9226]; `embed/gene_vectors.npy` [9226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9226 or target_col == 9226). Every well: [[R3HCC1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/R3HCC1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
