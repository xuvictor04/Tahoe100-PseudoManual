---
symbol: "VPS37A"
type: "gene"
col: 7937
ensembl_id: "ENSG00000155975"
name: "VPS37A subunit of ESCRT-I"
location: "8p22"
module: 109
arm: "+"
pooled_cpm: 62.84
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# VPS37A

*VPS37A subunit of ESCRT-I* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +13.5, q 9e-39, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.839× (z -6.4, q 1e-07, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (C-33 A 0.129×, HepG2/C3A 0.337×, KATO III 0.439×, CHP-212 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.115×, LS 180 0.339×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.145×, HepG2/C3A 0.321×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.496×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VIPAS39]] (+0.58, fdr 3e-05), [[LNPK]] (+0.58, fdr 1e-05), [[VPS35]] (+0.53, fdr 3e-05); moves opposite to [[NR4A1]] (-0.63, fdr 1e-05), [[IER2]] (-0.57, fdr 4e-05), [[PMEPA1]] (-0.51, fdr 4e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LNPK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +13.5 | 9e-39 | 34/48 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +13.4 | 3e-38 | 37/48 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +12.8 | 3e-35 | 36/49 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +12.3 | 1e-32 | 38/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +11.5 | 9e-29 | 36/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +11.4 | 7e-28 | 36/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +9.9 | 2e-21 | 39/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +9.8 | 6e-21 | 35/48 (HOP62, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +9.6 | 5e-20 | 38/48 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +9.5 | 1e-19 | 37/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.3 | 6e-15 | 35/48 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.1 | 3e-14 | 34/50 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +8.0 | 7e-14 | 28/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.9 | 1e-13 | 31/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.7 | 4e-07 | 18/48 (A-427, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +4.5 | 2e-04 | 21/49 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.2 | 9e-04 | 6/49 (SK-MEL-2, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7937.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (C-33 A 0.129×, HepG2/C3A 0.337×, KATO III 0.439×, CHP-212 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.115×, LS 180 0.339×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.145×, HepG2/C3A 0.321×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.496×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -6.4 | 1e-07 | 18/48 (LS 180, SW 900, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.763×** | -4.9 | 2e-04 | 24/47 (LoVo, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.829×** | -4.8 | 3e-04 | 20/49 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.891× | -4.2 | 0.004 | 6/48 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.853× | -4.1 | 0.005 | 19/48 (Hs 766T, A-427, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.766×** | -3.6 | 0.035 | 18/45 (H4, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.872× | -3.5 | 0.036 | 21/48 (RKO, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.868× | -3.3 | 0.057 | 19/45 (C-33 A, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.886× | -3.1 | 0.12 | 6/48 (RPMI-7951, C-33 A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 84.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.01× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -26.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 39.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.6) | — |
| [[SW480 (line)]] | alt | 67.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 99.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 140 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.496× (z -8.9) |
| [[PANC-1 (line)]] | alt | 23.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 46.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 68.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.1) | — |
| [[LoVo (line)]] | wt | 56.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 58.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.8) | — |
| [[A-172 (line)]] | wt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.0) | — |
| [[A498 (line)]] | wt | 92.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.98× (z +9.9) | — |
| [[A549 (line)]] | wt | 71.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 54.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.0) | — |
| [[J82 (line)]] | alt | 43.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.6) | — |
| [[KATO III (line)]] | alt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 76.3 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.45× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 68.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 44.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.7) | — |
| [[RKO (line)]] | wt | 76.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 68.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 56.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 54.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIPAS39]] | +0.58 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[LNPK]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[VPS35]] | +0.53 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MRPL13]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PDCD6IP]] | +0.52 | +0.57 / +0.45 | both halves | 3e-05 | pathway: Budding and maturation of HIV virion; STRING 696 |
| [[PRDX6]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RNF14]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[APOOL]] | +0.51 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[UGP2]] | +0.50 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[TMED8]] | +0.50 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[IREB2]] | +0.49 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[COX15]] | +0.49 | +0.63 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR4A1]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[IER2]] | -0.57 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[PMEPA1]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[NRARP]] | -0.50 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[CSRNP1]] | -0.49 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[ZNF628]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[HES1]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MIR23AHG]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[SEMA3F]] | -0.47 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[IER3]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[JUNB]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[MAP2K3]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNPK]] | C | LNPK's natural level weakens VPS37A's drug response | LNPK's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.11; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction -0.498). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.6, 20.1); signed map (-32.3, -23.5). **Vector** length 78.2, 16.8% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +12.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +9.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.0 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.5 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | +4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | VPS37A subunit of ESCRT-I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,246,931-17,302,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32642, HCRP1, SPG53; previously PQBP2 |
| Gene groups (HGNC) | ESCRT-I |
| Reactome | 15 pathways, smallest: Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins; Assembly Of The HIV Virion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEZ2](https://www.uniprot.org/uniprotkb/Q8NEZ2) (Vacuolar protein sorting-associated protein 37A):

> Component of the ESCRT-I complex, a regulator of vesicular trafficking process. Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies. May be involved in cell growth and differentiation.

**Summary**, from NCBI Gene [137492](https://www.ncbi.nlm.nih.gov/gene/137492):

> This gene belongs to the VPS37 family, and encodes a component of the ESCRT-I (endosomal sorting complex required for transport I) protein complex, required for the sorting of ubiquitinated transmembrane proteins into internal vesicles of multivesicular bodies. Expression of this gene is downregulated in hepatocellular carcinoma, and mutations in this gene are associated with autosomal recessive spastic paraplegia-53. A related pseudogene has been identified on chromosome 5. Alternatively …

**Accessions** — [HGNC:24928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24928) · Entrez [137492](https://www.ncbi.nlm.nih.gov/gene/137492) · UniProt [Q8NEZ2](https://www.uniprot.org/uniprotkb/Q8NEZ2) · Ensembl [ENSG00000155975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155975)

## Data

Gene col 7937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7937); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7937]; `tensor/DDL_lfc|DDL_z.npy` [7937]; `embed/gene_vectors.npy` [7937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7937 or target_col == 7937). Every well: [[VPS37A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS37A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
