---
symbol: "PARD6G-AS1"
type: "gene"
col: 15538
ensembl_id: "ENSG00000267270"
name: "PARD6G antisense RNA 1"
location: "18q23"
module: 53
arm: "+"
pooled_cpm: 14.85
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PARD6G-AS1

*PARD6G antisense RNA 1* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.92× (z +18.5, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.671× (z -3.9, q 0.057, down in 25 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H23 0.0512×, RPMI-7951 0.0747×, NCI-H2347 0.0706×, SNU-423 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (H4 0.127×, NCI-H23 0.151×, A549 0.113×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.144×; ⚠ cell-cycle shift, explains ~56% of this change); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0507×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (A-172 0.0933×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (A-427 0.0518×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2D3-AS1]] (+0.81, fdr 7e-06), [[PTOV1-AS1]] (+0.81, fdr 7e-06), [[ZNF546]] (+0.78, fdr 7e-06); moves opposite to [[BRAT1]] (-0.68, fdr 3e-05), [[TUBG2]] (-0.68, fdr 1e-05), [[SLC9A6]] (-0.67, fdr 1e-04).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +18.5 | 0e+00 | 43/46 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.58×** | +18.1 | 0e+00 | 44/46 (PANC-1, C-33 A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +12.7 | 1e-34 | 42/47 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +8.7 | 7e-16 | 31/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +7.2 | 9e-11 | 32/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.99×** | +6.6 | 5e-09 | 40/48 (LoVo, A-427, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.9 | 4e-07 | 26/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.45×** | +5.0 | 5e-05 | 24/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.6 | 3e-04 | 27/46 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.61×** | +4.3 | 1e-03 | 20/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.48×** | +3.5 | 0.024 | 20/47 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.95×** | +3.3 | 0.039 | 13/47 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.041 | 19/47 (J82, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Infigratinib (drug)]] 5 µM |  | **1.93×** | +3.3 | 0.041 | 15/47 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.41×** | +3.2 | 0.059 | 17/44 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15538.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H23 0.0512×, RPMI-7951 0.0747×, NCI-H2347 0.0706×, SNU-423 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (H4 0.127×, NCI-H23 0.151×, A549 0.113×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.144×; ⚠ cell-cycle shift, explains ~56% of this change); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0507×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (A-172 0.0933×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (A-427 0.0518×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.671×** | -3.9 | 0.057 | 25/46 (NCI-H23, RPMI-7951, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.734× | -3.0 | 0.71 | 15/48 (PANC-1, H4, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.9 | 4 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 15.0× (z +18.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -13.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H460 (line)]] | wt | 17.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +20.5) | — |
| [[A-172 (line)]] | wt | 12.6 | 3 | 1 | [[Auranofin (drug)]] 5 µM 17.7× (z +14.2) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0933× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 17.9 | 2 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 15.3× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.0747× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.113× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0507× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 3 | 0 | [[Auranofin (drug)]] 5 µM 11.4× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.0512× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 6.80 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 26.1× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.0706× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW 900 (line)]] | alt | 15.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 12.8× (z +11.8) | — |
| [[A-427 (line)]] | wt | 6.39 | 1 | 1 | [[Auranofin (drug)]] 5 µM 9.95× (z +8.7) | [[Glycyrrhizic acid (drug)]] 5 µM 0.0518× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 8.02 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +11.0) | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0786× (z -9.8) |
| [[BT-474 (line)]] | alt | 17.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 15.0× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 47.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 19.1× (z +16.3) | — |
| [[CFPAC-1 (line)]] | alt | 8.15 | 2 | 0 | [[Auranofin (drug)]] 5 µM 13.7× (z +12.1) | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.132× (z -8.9) |
| [[HT-29 (line)]] | alt | 10.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 49.9× (z +16.0) | — |
| [[LoVo (line)]] | wt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +15.0) | — |
| [[RKO (line)]] | wt | 17.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.04× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +13.8) | — |
| [[SNU-423 (line)]] | alt | 16.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 9.83× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.128× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 7.71 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 18.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 36.8× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 7.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +10.5) | — |
| [[H4 (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 7.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 9.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 12.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.3× (z +11.7) | — |
| [[J82 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +14.4) | — |
| [[KATO III (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +14.8) | — |
| [[LS 180 (line)]] | wt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 7.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 7.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 4.83 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.0× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 31.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +11.5) | — |
| [[SW48 (line)]] | wt | 29.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 27.5× (z +13.7) | — |
| [[SW480 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.2) | — |
| [[A498 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2D3-AS1]] | +0.81 | +0.75 / +0.67 | both halves | 7e-06 | same gene group |
| [[PTOV1-AS1]] | +0.81 | +0.77 / +0.69 | both halves | 7e-06 | same gene group |
| [[ZNF546]] | +0.78 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[MPDU1]] | +0.77 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.77 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[MSH4]] | +0.76 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.76 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.76 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[IDI2-AS1]] | +0.76 | +0.81 / +0.61 | both halves | 7e-06 | same gene group |
| [[NUP210L]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[YIPF7]] | +0.75 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.75 | +0.77 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.68 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[TUBG2]] | -0.68 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.67 | -0.75 / -0.35 | both halves | 1e-04 |  |
| [[MALSU1]] | -0.65 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[LSM2]] | -0.65 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PARD6G-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity lowers PARD6G-AS1's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.65× higher at baseline in the lines without C21orf91-OT1 | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[ZNF382]] | B | ZNF382 activity raises PARD6G-AS1's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.52× lower at baseline in the lines without ZNF382 | 0.039 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[RNF217]] | B | RNF217 activity lowers PARD6G-AS1's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without RNF217 | 0.082 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.8, -11.9); signed map (21.8, -2.4). **Vector** length 101, 23.3% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.8 | +18.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +18.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.2 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +6.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.0 | -1.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | PARD6G antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18q23 — chr18:80,147,908-80,179,839 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44109) · Entrez [100130522](https://www.ncbi.nlm.nih.gov/gene/100130522) · Ensembl [ENSG00000267270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267270)

## Data

Gene col 15538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15538); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15538]; `tensor/DDL_lfc|DDL_z.npy` [15538]; `embed/gene_vectors.npy` [15538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15538 or target_col == 15538). Every well: [[PARD6G-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARD6G-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
