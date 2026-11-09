---
symbol: "MAP3K7"
type: "gene"
col: 5687
ensembl_id: "ENSG00000135341"
name: "mitogen-activated protein kinase kinase kinase 7"
location: "6q15"
module: 52
arm: "+"
pooled_cpm: 93.68
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# MAP3K7

*mitogen-activated protein kinase kinase kinase 7* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +11.3, q 6e-27, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.659× (z -8.5, q 1e-14, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.817× (z -6.1, q 3e-07, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 0.252×, SW1417 0.268×, SW 900 0.350×, A-427 0.437×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.334×, SK-MEL-2 0.368×, HCT15 0.341×, SW1417 0.446×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.386×, HEC-1-A 0.439×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.299×); [[Fluvoxamine (drug)]] 0.05 µM in 1 line (SW 1088 0.0800×); [[Valdecoxib (drug)]] 0.05 µM in 1 line (SW 1271 0.192×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGG]] (+0.65, fdr 1e-05), [[FAM120B]] (+0.64, fdr 9e-06), [[SLC30A7]] (+0.63, fdr 7e-06); moves opposite to [[CXADR]] (-0.58, fdr 1e-05), [[HMGN3]] (-0.58, fdr 1e-05), [[LRIG3]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +11.3 | 6e-27 | 34/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +8.2 | 9e-14 | 37/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +7.7 | 2e-12 | 37/48 (SHP-77, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.3 | 4e-11 | 29/49 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.23×** | +4.4 | 0.001 | 25/48 (SW480, SW48, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +4.3 | 0.002 | 25/48 (SNU-423, SW48, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.004 | 23/49 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.025 | 25/48 (KATO III, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.18× | +3.5 | 0.025 | 19/48 (SW48, A-172, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.025 | 22/49 (Panc 03.27, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.16× | +3.0 | 0.11 | 15/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.32× | +3.0 | 0.11 | 16/38 (NCI-H1573, SW 900, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5687.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 0.252×, SW1417 0.268×, SW 900 0.350×, A-427 0.437×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.334×, SK-MEL-2 0.368×, HCT15 0.341×, SW1417 0.446×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.386×, HEC-1-A 0.439×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.299×); [[Fluvoxamine (drug)]] 0.05 µM in 1 line (SW 1088 0.0800×); [[Valdecoxib (drug)]] 0.05 µM in 1 line (SW 1271 0.192×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -8.5 | 1e-14 | 35/44 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.694×** | -7.7 | 3e-12 | 38/49 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -6.1 | 3e-07 | 27/48 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.800×** | -4.4 | 0.002 | 23/45 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.866× | -4.3 | 0.002 | 13/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.821×** | -4.2 | 0.003 | 25/49 (SW480, RKO, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | 0.838× | -3.8 | 0.014 | 22/48 (RPMI-7951, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.892× | -3.5 | 0.040 | 6/48 (NCI-H1792, Hs 766T, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.789× | -3.1 | 0.11 | 17/48 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 121 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.2) | — |
| [[NCI-H460 (line)]] | wt | 79.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.477× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 148 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -11.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 84.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 95.1 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.150× (z -11.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -17.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 84.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 77.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.437× (z -9.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -9.2) |
| [[BT-474 (line)]] | alt | 91.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 76.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.7) | — |
| [[KATO III (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.390× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 88.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.294× (z -9.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 74.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.445× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 129 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.5) | — |
| [[RKO (line)]] | wt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.413× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 70.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.0) | — |
| [[SW 1088 (line)]] | alt | 90.8 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.05 µM 0.0800× (z -8.8) |
| [[SW 1271 (line)]] | alt | 130 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.192× (z -8.6) |
| [[SW 900 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 72.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.7) | — |
| [[A-172 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 71.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 100.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGG]] | +0.65 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[FAM120B]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[SLC30A7]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PRKAG1]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING; STRING 918 |
| [[DCTN5]] | +0.63 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[RECQL5]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[GPATCH2L]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ACAD9]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SENP5]] | +0.59 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[ADAMTSL4-AS2]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CCNT1]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.57 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXADR]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[LRIG3]] | -0.55 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[HSF2]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[KIF13A]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TMEM131L]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SMAD7]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING; STRING 595 |
| [[ARHGAP17]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SOAT1]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[TRAK1]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[USP2]] | -0.51 | -0.42 / -0.58 | both halves | 4e-05 | pathway: Death Receptor Signaling; STRING 600 |
| [[OSR2]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (19.4, -22.0); signed map (8.6, 14.0). **Vector** length 89.8, 22.1% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.5 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +8.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.5 | +1.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.4 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -5.4 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | +0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.7 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:90,513,573-90,587,086 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEKK7; previously TAK1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; Mixed lineage kinase family |
| Hallmark sets | TGF_BETA_SIGNALING, PI3K_AKT_MTOR_SIGNALING, ALLOGRAFT_REJECTION |
| Reactome | 56 pathways, smallest: IRAK2 mediated activation of TAK1 complex; Alpha-protein kinase 1 signaling pathway; TICAM1,TRAF6-dependent induction of TAK1 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O43318](https://www.uniprot.org/uniprotkb/O43318) (Mitogen-activated protein kinase kinase kinase 7):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. Plays an important role in the cascades of cellular responses evoked by changes in the environment. Mediates signal transduction of TRAF6, various cytokines including interleukin-1 (IL-1), transforming growth factor-beta (TGFB), TGFB-related factors like BMP2 and BMP4, toll-like receptors (TLR), tumor necrosis factor receptor CD40 and B-cell receptor (BCR). Once activated, acts as an …

**Summary**, from NCBI Gene [6885](https://www.ncbi.nlm.nih.gov/gene/6885):

> The protein encoded by this gene is a member of the serine/threonine protein kinase family. This kinase mediates the signaling transduction induced by TGF beta and morphogenetic protein (BMP), and controls a variety of cell functions including transcription regulation and apoptosis. In response to IL-1, this protein forms a kinase complex including TRAF6, MAP3K7P1/TAB1 and MAP3K7P2/TAB2; this complex is required for the activation of nuclear factor kappa B. This kinase can also activate …

**Accessions** — [HGNC:6859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6859) · Entrez [6885](https://www.ncbi.nlm.nih.gov/gene/6885) · UniProt [O43318](https://www.uniprot.org/uniprotkb/O43318) · Ensembl [ENSG00000135341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135341)

## Data

Gene col 5687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5687); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5687]; `tensor/DDL_lfc|DDL_z.npy` [5687]; `embed/gene_vectors.npy` [5687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5687 or target_col == 5687). Every well: [[MAP3K7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
