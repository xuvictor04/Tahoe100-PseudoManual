---
symbol: "PDRG1"
type: "gene"
col: 1530
ensembl_id: "ENSG00000088356"
name: "p53 and DNA damage regulated 1"
location: "20q11.21"
module: 11
arm: "+"
pooled_cpm: 19.12
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PDRG1

*p53 and DNA damage regulated 1* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.96× (z +18.2, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.87× (z +17.4, q 0e+00, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.189×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0994×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0725×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSUN5]] (+0.81, fdr 7e-06), [[PHAX]] (+0.76, fdr 7e-06), [[GSPT2]] (+0.75, fdr 7e-06); moves opposite to [[STT3B]] (-0.69, fdr 7e-06), [[TM9SF3]] (-0.65, fdr 7e-06), [[PDIA6]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF727]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.96×** | +18.2 | 0e+00 | 46/47 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.87×** | +17.4 | 0e+00 | 46/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.16×** | +14.2 | 2e-43 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.68×** | +12.6 | 2e-34 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.32×** | +10.8 | 5e-25 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +9.3 | 2e-18 | 38/43 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.02×** | +9.0 | 2e-17 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +8.7 | 2e-16 | 39/47 (SW480, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +8.3 | 8e-15 | 39/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.87×** | +8.0 | 5e-14 | 38/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.79×** | +7.4 | 5e-12 | 36/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.78×** | +7.4 | 7e-12 | 40/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.77×** | +7.3 | 1e-11 | 39/47 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +7.1 | 6e-11 | 36/47 (PANC-1, J82, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.74×** | +6.8 | 3e-10 | 28/43 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +5.0 | 2e-05 | 28/47 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.6 | 1e-04 | 23/46 (NCI-H460, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.2 | 6e-04 | 23/48 (CFPAC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.011 | 15/47 (RPMI-7951, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.012 | 15/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.049 | 15/47 (HEC-1-A, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1530.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.189×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0994×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -3.9 | 0.053 | 4/48 (hTERT-HPNE, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.4 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +16.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.77× (z +15.4) | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +11.4) | — |
| [[SW480 (line)]] | alt | 22.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.43× (z +10.2) | — |
| [[A498 (line)]] | wt | 19.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +14.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.03× (z +12.5) | — |
| [[A549 (line)]] | wt | 12.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.75× (z +10.3) | — |
| [[J82 (line)]] | alt | 41.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +10.2) | — |
| [[A-172 (line)]] | wt | 12.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.27× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.18× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 19.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 20.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.27× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 17.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.71× (z +10.6) | — |
| [[KATO III (line)]] | alt | 27.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.40× (z +11.0) | — |
| [[LoVo (line)]] | wt | 9.73 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.24× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.57× (z +9.9) | — |
| [[A-427 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 10.1 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0725× (z -8.5) |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0994× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.77× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.87× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.73× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5]] | +0.81 | +0.70 / +0.86 | both halves | 7e-06 |  |
| [[PHAX]] | +0.76 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.75 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.75 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[COIL]] | +0.74 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.73 | +0.67 / +0.82 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[ZNF182]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[TMEM70]] | +0.71 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.71 | +0.71 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.69 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[TM9SF3]] | -0.65 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[PDIA6]] | -0.63 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.63 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[IMPA2]] | -0.62 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.62 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.62 | -0.61 / -0.57 | both halves | 8e-06 |  |
| [[RCN2]] | -0.61 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[RPN1]] | -0.61 | -0.54 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF727]] | B | ZNF727 activity raises PDRG1's level | lines that do not express ZNF727 (35) vs lines expressing it (15) | 1.24× lower at baseline in the lines without ZNF727 | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF732, CCK, LINC02899 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.2, 3.9); signed map (0.0, -22.7). **Vector** length 71.8, 15.7% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +17.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.1 | +14.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +8.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +7.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.5 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.3 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | +1.6 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | +2.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | p53 and DNA damage regulated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:31,944,337-31,952,046 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ310O13.3; previously C20orf126 |
| Gene groups (HGNC) | Prefoldin-like complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUG6](https://www.uniprot.org/uniprotkb/Q9NUG6) (p53 and DNA damage-regulated protein 1):

> May play a role in chaperone-mediated protein folding.

**Summary**, from NCBI Gene [81572](https://www.ncbi.nlm.nih.gov/gene/81572):

> Predicted to enable unfolded protein binding activity. Predicted to be involved in protein folding and protein stabilization. Predicted to be located in cytoplasm. Predicted to be part of prefoldin complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16119) · Entrez [81572](https://www.ncbi.nlm.nih.gov/gene/81572) · UniProt [Q9NUG6](https://www.uniprot.org/uniprotkb/Q9NUG6) · Ensembl [ENSG00000088356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088356)

## Data

Gene col 1530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1530); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1530]; `tensor/DDL_lfc|DDL_z.npy` [1530]; `embed/gene_vectors.npy` [1530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1530 or target_col == 1530). Every well: [[PDRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
