---
symbol: "GSE1"
type: "gene"
col: 5177
ensembl_id: "ENSG00000131149"
name: "Gse1 coiled-coil protein"
location: "16q24.1"
module: 14
arm: "+"
pooled_cpm: 154.65
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# GSE1

*Gse1 coiled-coil protein* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.26× (z +4.4, q 0.005, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (NCI-H1792 5.24×, A498 2.33×, SW1417 2.37×, SNU-423 2.95×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 2.83×, NCI-H460 2.47×, LS 180 2.04×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A498 5.06×, NCI-H460 3.94×, A549 2.90×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (KATO III 1.59×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.607× (z -9.6, q 4e-19, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAHCC1]] (+0.72, fdr 7e-06), [[NFIX]] (+0.62, fdr 1e-05), [[STK11]] (+0.61, fdr 1e-05); moves opposite to [[HEATR5B]] (-0.53, fdr 1e-04), [[LCMT1]] (-0.53, fdr 1e-04), [[TRIP4]] (-0.53, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CBFA2T3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5177.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (NCI-H1792 5.24×, A498 2.33×, SW1417 2.37×, SNU-423 2.95×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 2.83×, NCI-H460 2.47×, LS 180 2.04×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A498 5.06×, NCI-H460 3.94×, A549 2.90×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (KATO III 1.59×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 0.005 | 28/48 (A-172, NCI-H460, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.3 | 0.005 | 22/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.7 | 0.046 | 20/48 (NCI-H1792, A498, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.054 | 23/48 (A-172, PANC-1, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.22× | +3.2 | 0.18 | 18/47 (A-172, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.19 | 15/47 (A498, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.607×** | -9.6 | 4e-19 | 42/48 (NCI-H23, C-33 A, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.635×** | -8.7 | 7e-16 | 35/48 (NCI-H23, SNU-1, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -8.6 | 1e-15 | 36/48 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -8.5 | 4e-15 | 35/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.658×** | -7.6 | 3e-12 | 36/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -7.0 | 3e-10 | 32/47 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.539×** | -6.2 | 4e-08 | 35/45 (SNU-423, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -5.9 | 2e-07 | 29/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.753×** | -5.0 | 3e-05 | 26/45 (RKO, C-33 A, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.807×** | -4.1 | 0.002 | 26/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -4.0 | 0.003 | 22/48 (NCI-H1573, CHP-212, …) | top dose only | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.787×** | -3.8 | 0.007 | 24/47 (HOP62, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.691×** | -3.7 | 0.009 | 23/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.835× | -3.5 | 0.022 | 22/48 (CHP-212, SHP-77, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.722×** | -3.3 | 0.040 | 19/49 (NCI-H23, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.744×** | -3.0 | 0.094 | 18/48 (SNU-423, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 232 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.380× (z -11.1) |
| [[HT-29 (line)]] | alt | 312 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.350× (z -10.0) |
| [[SNU-1 (line)]] | wt | 399 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -11.4) |
| [[A498 (line)]] | wt | 130 | 4 (4 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +17.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 179 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.59× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.463× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 215 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -16.2) |
| [[PANC-1 (line)]] | alt | 242 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.416× (z -9.8) |
| [[A-427 (line)]] | wt | 223 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -9.8) |
| [[COLO 205 (line)]] | alt | 192 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -11.1) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.443× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 131 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.295× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 75.0 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +17.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 252 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0584× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SHP-77 (line)]] | alt | 297 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.467× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.493× (z -8.6) |
| [[A549 (line)]] | wt | 117 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +18.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 636 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 333 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.356× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 63.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.220× (z -14.0) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.357× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +25.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 72.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.400× (z -8.7) |
| [[SW1417 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 170 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.432× (z -8.5) |
| [[C32 (line)]] | wt | 136 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 303 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -8.8) |
| [[HOP62 (line)]] | alt | 197 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.265× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 70.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 155 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.489× (z -10.0) |
| [[LS 180 (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.356× (z -10.0) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 61.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 60.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 70.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 92.9 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.417× (z -8.6) |
| [[SW 1271 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0698× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 401 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 95.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAHCC1]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[NFIX]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[STK11]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[BCOR]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ERF]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[RAI1]] | +0.58 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[AJUBA]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[RCC2]] | +0.56 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SLC12A7]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[HNRNPL]] | +0.55 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[ELFN1]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PIEZO1]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR5B]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[LCMT1]] | -0.53 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[TRIP4]] | -0.53 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ARPC1A]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[RAB18]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[DNAJC24]] | -0.50 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[MED23]] | -0.50 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[RARS2]] | -0.50 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[DHDDS]] | -0.50 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[SLC25A14]] | -0.49 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[EYA3]] | -0.49 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[WDR37]] | -0.49 | -0.52 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBFA2T3]] | B | CBFA2T3 activity raises GSE1's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without CBFA2T3 | 0.008 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[SOBP]] | B | SOBP activity raises GSE1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without SOBP | 0.046 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[ELFN1]] | B | ELFN1 activity raises GSE1's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without ELFN1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[SAMD11]] | B | SAMD11 activity raises GSE1's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without SAMD11 | 0.099 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.434). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.3, -2.5); signed map (29.0, -36.5). **Vector** length 119, 34.6% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.2 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +4.5 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Gse1 coiled-coil protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:85,169,525-85,676,204 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0182 |
| Matched by | ensembl_id |

UniProt [Q14687](https://www.uniprot.org/uniprotkb/Q14687) carries no function annotation.

**Summary**, from NCBI Gene [23199](https://www.ncbi.nlm.nih.gov/gene/23199):

> This gene encodes a proline-rich protein with coiled coil domains that may be a subunit of a BRAF35-HDAC (BHC) histone deacetylase complex. This gene may function as an oncogene in breast cancer and enhanced expression of the encoded protein has been observed in breast cancer patients. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:28979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28979) · Entrez [23199](https://www.ncbi.nlm.nih.gov/gene/23199) · UniProt [Q14687](https://www.uniprot.org/uniprotkb/Q14687) · Ensembl [ENSG00000131149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131149)

## Data

Gene col 5177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5177); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5177]; `tensor/DDL_lfc|DDL_z.npy` [5177]; `embed/gene_vectors.npy` [5177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5177 or target_col == 5177). Every well: [[GSE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
