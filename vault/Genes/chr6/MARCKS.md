---
symbol: "MARCKS"
type: "gene"
col: 15892
ensembl_id: "ENSG00000277443"
name: "myristoylated alanine rich protein kinase C substrate"
location: "6q21"
module: 14
arm: "+"
pooled_cpm: 212.08
n_lines_expressing: 40
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# MARCKS

*myristoylated alanine rich protein kinase C substrate* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.16× (z +7.8, q 3e-12, up in 35 of 38 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Cyclosporin A (drug)]] 0.05 µM: 1.38× (z +3.4, q 0.055, up in 30 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 5 lines (BT-474 4.15×, A549 3.40×, SNU-423 2.66×, NCI-H1792 3.19×, …; ⚠ cell-cycle shift, explains ~51% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (BT-474 3.95×, AsPC-1 2.24×, Panc 03.27 2.33×, A549 2.16×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A549 3.79×, C32 3.28×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 2.81×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.293× (z -12.9, q 2e-35, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR3C1]] (+0.70, fdr 7e-06), [[SLC2A6]] (+0.69, fdr 7e-06), [[CCL5]] (+0.68, fdr 1e-05); moves opposite to [[MTRR]] (-0.61, fdr 1e-05), [[WDR5]] (-0.61, fdr 1e-05), [[LY6G5B]] (-0.60, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SMAD7]] → it (grade B ⚠); 12 go from it, the strongest it → [[KMT2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15892.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 5 lines (BT-474 4.15×, A549 3.40×, SNU-423 2.66×, NCI-H1792 3.19×, …; ⚠ cell-cycle shift, explains ~51% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (BT-474 3.95×, AsPC-1 2.24×, Panc 03.27 2.33×, A549 2.16×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A549 3.79×, C32 3.28×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 2.81×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.16×** | +7.8 | 3e-12 | 35/38 (BT-474, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +4.8 | 4e-04 | 23/38 (BT-474, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.52×** | +4.5 | 0.002 | 30/38 (AsPC-1, KATO III, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.55×** | +4.4 | 0.002 | 26/38 (A549, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.41×** | +3.7 | 0.029 | 22/38 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~95% of this change | **1.39×** | +3.5 | 0.051 | 27/38 (SW480, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.055 | 30/39 (A-172, C32, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.293×** | -12.9 | 2e-35 | 38/38 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.332×** | -11.6 | 1e-28 | 38/38 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.392×** | -9.8 | 1e-20 | 38/38 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.589×** | -7.8 | 6e-13 | 27/39 (A-172, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.578×** | -5.4 | 6e-06 | 32/38 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.604×** | -5.3 | 1e-05 | 34/38 (A498, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.642×** | -4.5 | 6e-04 | 27/38 (HS-578T, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.659×** | -4.4 | 8e-04 | 29/38 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.471×** | -4.1 | 0.002 | 31/39 (A-172, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.694×** | -3.8 | 0.007 | 31/38 (A498, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.723×** | -3.4 | 0.036 | 22/38 (A-172, HS-578T, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.730×** | -3.3 | 0.047 | 28/38 (A498, HS-578T, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **0.555×** | -3.2 | 0.053 | 21/35 (J82, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -3.2 | 0.054 | 21/38 (PANC-1, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -3.2 | 0.054 | 23/38 (HepG2/C3A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.739×** | -3.2 | 0.054 | 24/38 (HS-578T, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.83 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 286 | 2 (2 ⚠) | 6 | [[Harringtonine (drug)]] 0.5 µM 3.01× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 5 µM 0.254× (z -11.8) |
| [[HS-578T (line)]] | alt | 593 | 2 (2 ⚠) | 6 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.82× (z +8.9) ⚠ cell-cycle shift, explains ~51% of this change | [[Panobinostat (drug)]] 5 µM 0.202× (z -14.2) |
| [[A549 (line)]] | wt | 281 | 3 (3 ⚠) | 3 | [[Harringtonine (drug)]] 0.5 µM 3.79× (z +10.6) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 5 µM 0.191× (z -13.8) |
| [[C32 (line)]] | wt | 290 | 2 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.28× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.81× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.230× (z -12.6) |
| [[A-172 (line)]] | wt | 548 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -17.8) |
| [[AsPC-1 (line)]] | alt | 217 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.324× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 524 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -13.8) |
| [[SNU-423 (line)]] | alt | 1,066 | 1 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.66× (z +9.4) ⚠ cell-cycle shift, explains ~51% of this change | [[Panobinostat (drug)]] 5 µM 0.241× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 78.7 | 1 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 3.25× (z +8.5) ⚠ cell-cycle shift, explains ~51% of this change | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 86.6 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 3.24× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 384 | 1 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.19× (z +9.4) ⚠ cell-cycle shift, explains ~51% of this change | [[Panobinostat (drug)]] 5 µM 0.233× (z -12.3) |
| [[BT-474 (line)]] | alt | 182 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +15.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 256 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -12.3) |
| [[H4 (line)]] | wt | 185 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.270× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 505 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -13.9) |
| [[HOP62 (line)]] | alt | 234 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -12.5) |
| [[Hs 766T (line)]] | wt | 395 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -14.6) |
| [[KATO III (line)]] | alt | 148 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.24× (z +9.7) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 152 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.265× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 332 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -10.9) |
| [[CHP-212 (line)]] | wt | 277 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -10.3) |
| [[J82 (line)]] | alt | 649 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 227 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 204 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.19× (z +9.4) ⚠ cell-cycle shift, explains ~51% of this change | [[Panobinostat (drug)]] 5 µM 0.364× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 206 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.485× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.370× (z -8.9) |
| [[PANC-1 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.37× (z +8.7) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 224 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 133 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -9.2) |
| [[SW 900 (line)]] | alt | 185 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -10.0) |
| [[A-427 (line)]] | wt | 25.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 52.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 31.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 436 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 66.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR3C1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SLC2A6]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CCL5]] | +0.68 | +0.53 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SLC41A2]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[GATA6]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TUBB2A]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GBP5]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[C15orf48]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[MSC]] | +0.63 | +0.52 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BTG1]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[LINC02968]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RRAD]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRR]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[WDR5]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[LY6G5B]] | -0.60 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[TMEM181]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[GCN1]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TIMM10B]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[THOC5]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[NSUN2]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[INTS11]] | -0.57 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD7]] | B | SMAD7 activity raises MARCKS's level | lines that do not express SMAD7 (5) vs lines expressing it (45) | 6.31× lower at baseline in the lines without SMAD7 | 0.013 | ⚠ within organs, on part of the lines; also absent: SFXN3, KIAA2012, PLSCR2; maybe low, not absent |
| [[IL32]] | B | IL32 activity raises MARCKS's level | lines that do not express IL32 (18) vs lines expressing it (32) | 2.18× lower at baseline in the lines without IL32 | 0.022 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[ATXN1]] | B | ATXN1 activity raises MARCKS's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 4.02× lower at baseline in the lines without ATXN1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[GPR176]] | B | GPR176 activity raises MARCKS's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 3.38× lower at baseline in the lines without GPR176 | 0.058 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[RRAD]] | B | RRAD activity raises MARCKS's level | lines that do not express RRAD (31) vs lines expressing it (19) | 3.23× lower at baseline in the lines without RRAD | 0.069 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[COL1A1]] | B | COL1A1 activity raises MARCKS's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without COL1A1 | 0.073 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[TNFRSF9]] | B | TNFRSF9 activity raises MARCKS's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 3.27× lower at baseline in the lines without TNFRSF9 | 0.083 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[RND1]] | B | RND1 activity raises MARCKS's level | lines that do not express RND1 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without RND1 | 0.088 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[IRAG2]] | B | IRAG2 activity raises MARCKS's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.84× lower at baseline in the lines without IRAG2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[NFATC2]] | B | NFATC2 activity raises MARCKS's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without NFATC2 | 0.098 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KMT2A]] | B | MARCKS activity raises KMT2A's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without MARCKS | 0.004 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[CCDC148]] | B | MARCKS activity raises CCDC148's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without MARCKS | 0.038 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[KIAA0408]] | B | MARCKS activity raises KIAA0408's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 3.96× lower at baseline in the lines without MARCKS | 0.048 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[NFATC2]] | B | MARCKS activity raises NFATC2's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 3.42× lower at baseline in the lines without MARCKS | 0.057 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[RND1]] | B | MARCKS activity raises RND1's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without MARCKS | 0.079 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[PIM3]] | B | MARCKS activity raises PIM3's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without MARCKS | 0.081 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | B | MARCKS activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express MARCKS (10) vs lines expressing it (38) | the lines without MARCKS: 0.74× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[CADM1]] | B | MARCKS activity raises CADM1's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 3.96× lower at baseline in the lines without MARCKS | 0.084 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[LMNA]] | B | MARCKS activity raises LMNA's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without MARCKS | 0.085 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[CX3CL1]] | B | MARCKS activity raises CX3CL1's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without MARCKS | 0.097 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[RND3]] | B | MARCKS activity raises RND3's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without MARCKS | 0.097 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[MED19]] | B | MARCKS activity raises MED19's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.23× lower at baseline in the lines without MARCKS | 0.097 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 2.4); signed map (44.4, 10.8). **Vector** length 123, 42.9% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +9.6 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.4 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +6.2 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +2.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.2 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.0 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | myristoylated alanine rich protein kinase C substrate |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:113,857,345-113,863,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKCSL, 80K-L; previously MACS |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB, G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 3 pathways, smallest: Acetylcholine regulates insulin secretion; Regulation of insulin secretion; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P29966](https://www.uniprot.org/uniprotkb/P29966) (Myristoylated alanine-rich C-kinase substrate):

> Membrane-associated protein that plays a role in the structural modulation of the actin cytoskeleton, chemotaxis, motility, cell adhesion, phagocytosis, and exocytosis through lipid sequestering and/or protein docking to membranes. Thus, exerts an influence on a plethora of physiological processes, such as embryonic development, tissue regeneration, neuronal plasticity, and inflammation. Sequesters phosphatidylinositol 4,5-bisphosphate (PIP2) at lipid rafts in the plasma membrane of quiescent …

**Summary**, from NCBI Gene [4082](https://www.ncbi.nlm.nih.gov/gene/4082):

> The protein encoded by this gene is a substrate for protein kinase C. It is localized to the plasma membrane and is an actin filament crosslinking protein. Phosphorylation by protein kinase C or binding to calcium-calmodulin inhibits its association with actin and with the plasma membrane, leading to its presence in the cytoplasm. The protein is thought to be involved in cell motility, phagocytosis, membrane trafficking and mitogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6759) · Entrez [4082](https://www.ncbi.nlm.nih.gov/gene/4082) · UniProt [P29966](https://www.uniprot.org/uniprotkb/P29966) · Ensembl [ENSG00000277443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277443)

## Data

Gene col 15892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15892); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15892]; `tensor/DDL_lfc|DDL_z.npy` [15892]; `embed/gene_vectors.npy` [15892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15892 or target_col == 15892). Every well: [[MARCKS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCKS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
