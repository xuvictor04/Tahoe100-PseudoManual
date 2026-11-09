---
symbol: "PSMC5"
type: "gene"
col: 1489
ensembl_id: "ENSG00000087191"
name: "proteasome 26S subunit, ATPase 5"
location: "17q23.3"
module: 64
arm: "+"
pooled_cpm: 34.5
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMC5

*proteasome 26S subunit, ATPase 5* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.32× (z +13.8, q 8e-41, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.88× (z +12.2, q 1e-31, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 5 µM in 1 line (AN3 CA 0.0799×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC3]] (+0.81, fdr 7e-06), [[PSMD6]] (+0.81, fdr 7e-06), [[PSMD11]] (+0.76, fdr 7e-06); moves opposite to [[IGFBP2]] (-0.61, fdr 2e-05), [[PTMA]] (-0.57, fdr 2e-05), [[TMSB10]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.32×** | +13.8 | 8e-41 | 43/43 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.88×** | +12.2 | 1e-31 | 47/48 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.86×** | +11.6 | 5e-29 | 36/39 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.69×** | +11.4 | 6e-28 | 47/47 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.46×** | +9.8 | 1e-20 | 47/48 (NCI-H1792, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.47×** | +9.6 | 6e-20 | 39/43 (A-427, A498, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.22×** | +9.2 | 3e-18 | 47/47 (COLO 205, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.11×** | +8.6 | 6e-16 | 47/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.14×** | +8.4 | 2e-15 | 44/48 (A-427, SW480, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +6.3 | 2e-08 | 41/47 (CFPAC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +6.1 | 5e-08 | 38/47 (NCI-H1792, KATO III, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.62×** | +5.6 | 1e-06 | 38/46 (HT-29, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.34×** | +4.5 | 3e-04 | 29/47 (A549, HEC-1-A, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.45×** | +4.1 | 0.002 | 27/47 (C32, Panc 03.27, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.004 | 24/48 (LOX-IMVI, A549, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.007 | 24/48 (HEC-1-A, A549, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.007 | 27/48 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.056 | 16/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.069 | 18/47 (AsPC-1, KATO III, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +2.9 | 0.091 | 11/46 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1489.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 5 µM in 1 line (AN3 CA 0.0799×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.764× | -3.1 | 0.88 | 18/48 (A498, HOP62, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 31.3 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.06× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 34.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.67× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 26.8 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.60× (z +9.6) | — |
| [[A-427 (line)]] | wt | 53.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.33× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 42.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 36.3 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.57× (z +9.0) | — |
| [[KATO III (line)]] | alt | 46.2 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.37× (z +10.1) | — |
| [[SW480 (line)]] | alt | 37.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.92× (z +9.2) | — |
| [[A549 (line)]] | wt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 28.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.65× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 49.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.22× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 32.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.63× (z +9.0) | — |
| [[LoVo (line)]] | wt | 22.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 34.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.69× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 22.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 39.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.23× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 33.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.79× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 39.1 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0799× (z -9.3) |
| [[H4 (line)]] | wt | 34.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.93× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HS-578T (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[J82 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1573 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 900 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC3]] | +0.81 | +0.86 / +0.73 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD6]] | +0.81 | +0.87 / +0.75 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD11]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD4]] | +0.71 | +0.77 / +0.64 | both halves | 7e-06 | same gene group; pathway: Proteasome assembly; STRING 999 |
| [[PSMC4]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[CCT7]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 | STRING 765 |
| [[MRPL45]] | +0.67 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[PSMD7]] | +0.66 | +0.72 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC1]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[DPP3]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 | pathway: Cellular response to chemical stress |
| [[ANXA7]] | +0.63 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ALOX12P2-1]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP2]] | -0.61 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[PTMA]] | -0.57 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TMSB10]] | -0.57 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[DCAF11]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 | pathway: Neddylation |
| [[CD9]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[B3GAT3]] | -0.54 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[METRN]] | -0.54 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[NDUFA2]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NCK1-DT]] | -0.53 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[MHENCR]] | -0.53 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[CST3]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-22.7, -9.8); signed map (-6.5, -36.0). **Vector** length 88.7, 26.9% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +12.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.1 | +11.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.8 | +9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.5 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +9.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.2 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, ATPase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,827,152-63,832,026 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SUG1, p45/SUG, TBP10, p45, S8, TRIP1, SUG-1, RPT6 |
| Gene groups (HGNC) | AAA ATPases; Proteasome |
| Reactome | 169 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [P62195](https://www.uniprot.org/uniprotkb/P62195) (26S proteasome regulatory subunit 8):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. PSMC5 belongs to …

**Summary**, from NCBI Gene [5705](https://www.ncbi.nlm.nih.gov/gene/5705):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9552](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9552) · Entrez [5705](https://www.ncbi.nlm.nih.gov/gene/5705) · UniProt [P62195](https://www.uniprot.org/uniprotkb/P62195) · Ensembl [ENSG00000087191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087191)

## Data

Gene col 1489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1489); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1489]; `tensor/DDL_lfc|DDL_z.npy` [1489]; `embed/gene_vectors.npy` [1489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1489 or target_col == 1489). Every well: [[PSMC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
