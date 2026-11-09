---
symbol: "CIT"
type: "gene"
col: 4390
ensembl_id: "ENSG00000122966"
name: "citron rho-interacting serine/threonine kinase"
location: "12q24.23"
module: 67
arm: "+"
pooled_cpm: 103.49
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 37
n_dd_up_clean: 1
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CIT

*citron rho-interacting serine/threonine kinase* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 2.00× (z +6.0, q 8e-07, up in 32 of 46 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 1.59× (z +4.0, q 0.010, up in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 4.30×, C32 3.81×); [[Harringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 3.84×).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.487× (z -16.9, q 0e+00, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBK]] (+0.91, fdr 7e-06), [[CENPI]] (+0.91, fdr 7e-06), [[AURKB]] (+0.90, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CDC25C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4390.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 4.30×, C32 3.81×); [[Harringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 3.84×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.00×** | +6.0 | 8e-07 | 32/46 (NCI-H2347, J82, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.39×** | +5.5 | 9e-06 | 28/46 (A549, PANC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.010 | 22/47 (NCI-H2347, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.24×** | +3.6 | 0.054 | 20/47 (C32, LoVo, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.21× | +3.3 | 0.13 | 17/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.20× | +3.0 | 0.18 | 13/47 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.20× | +3.0 | 0.18 | 16/47 (RKO, A498, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.0 | 0.18 | 12/47 (NCI-H1792, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.487×** | -16.9 | 0e+00 | 35/47 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.501×** | -16.2 | 0e+00 | 40/47 (LOX-IMVI, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.402×** | -15.2 | 0e+00 | 44/47 (HEC-1-A, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -14.4 | 8e-45 | 38/47 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.572×** | -13.1 | 3e-37 | 42/47 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.490×** | -11.9 | 2e-30 | 43/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.486×** | -11.3 | 8e-28 | 41/47 (NCI-H2347, HT-29, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.527×** | -10.2 | 1e-22 | 38/47 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.545×** | -10.1 | 4e-22 | 39/47 (AN3 CA, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.563×** | -9.2 | 3e-18 | 36/46 (H4, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.579×** | -9.1 | 6e-18 | 33/47 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.598×** | -8.5 | 7e-16 | 35/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.708×** | -8.1 | 3e-14 | 31/47 (A-427, A549, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.721×** | -7.7 | 7e-13 | 30/47 (A-172, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.648×** | -7.2 | 2e-11 | 32/47 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.585×** | -4.7 | 9e-05 | 26/47 (SW480, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **0.825×** | -4.5 | 2e-04 | 26/47 (HT-29, Hs 766T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.758×** | -4.4 | 3e-04 | 19/47 (HS-578T, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -4.4 | 3e-04 | 24/47 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.608×** | -4.3 | 4e-04 | 22/48 (SW48, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 102 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.195× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 99.5 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.0) |
| [[LS 180 (line)]] | wt | 77.6 | 0 | 13 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.170× (z -16.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.228× (z -13.9) |
| [[H4 (line)]] | wt | 176 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0394× (z -20.5) |
| [[A498 (line)]] | wt | 74.1 | 0 | 10 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.217× (z -18.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 10 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.148× (z -19.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.175× (z -12.5) |
| [[SW48 (line)]] | wt | 126 | 0 | 10 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.284× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 124 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -22.5) |
| [[A-172 (line)]] | wt | 99.6 | 0 | 7 (4 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.134× (z -19.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.213× (z -14.7) |
| [[A-427 (line)]] | wt | 153 | 0 | 7 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.269× (z -17.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.301× (z -15.9) |
| [[LoVo (line)]] | wt | 85.4 | 0 | 7 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.371× (z -12.4) |
| [[HOP62 (line)]] | alt | 172 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 137 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0283× (z -27.0) |
| [[NCI-H2347 (line)]] | alt | 109 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.324× (z -17.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -10.7) |
| [[HCT15 (line)]] | alt | 157 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.124× (z -14.5) |
| [[HT-29 (line)]] | alt | 70.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 91.6 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.188× (z -11.1) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.371× (z -9.2) |
| [[J82 (line)]] | alt | 122 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.7) |
| [[SNU-1 (line)]] | wt | 114 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -14.7) |
| [[Hs 766T (line)]] | wt | 68.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.6) |
| [[AN3 CA (line)]] | alt | 181 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.0634× (z -19.3) |
| [[CFPAC-1 (line)]] | alt | 67.2 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.345× (z -11.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.7) |
| [[KATO III (line)]] | alt | 78.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 42.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 61.1 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.479× (z -9.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -8.9) |
| [[PANC-1 (line)]] | alt | 109 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 202 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +20.6) | [[Auranofin (drug)]] 5 µM 0.278× (z -12.7) |
| [[SW 900 (line)]] | alt | 121 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.299× (z -9.5) |
| [[SW480 (line)]] | alt | 156 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -17.1) |
| [[C32 (line)]] | wt | 113 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +15.2) | [[Selinexor (drug)]] 5 µM 0.425× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 163 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.330× (z -10.2) |
| [[C-33 A (line)]] | alt | 79.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.343× (z -9.4) |
| [[CHP-212 (line)]] | wt | 69.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0602× (z -10.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 54.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -9.8) |
| [[HS-578T (line)]] | alt | 58.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -8.6) |
| [[SNU-423 (line)]] | alt | 83.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.306× (z -9.9) |
| [[SW1417 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.549× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBK]] | +0.91 | +0.89 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[CENPI]] | +0.91 | +0.90 / +0.88 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[AURKB]] | +0.90 | +0.89 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 487 |
| [[RACGAP1]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 639 |
| [[BUB1B]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 407 |
| [[INCENP]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 691 |
| [[CDCA3]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[KIFC1]] | +0.89 | +0.87 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[KIF4A]] | +0.89 | +0.86 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 809 |
| [[PARPBP]] | +0.89 | +0.86 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[NCAPH]] | +0.89 | +0.86 / +0.87 | both halves | 7e-06 |  |
| [[DEPDC1B]] | +0.89 | +0.83 / +0.91 | both halves | 7e-06 | pathway: RAC1 GTPase cycle; STRING 492 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CIT's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without PIMREG | 0.025 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CIT's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NDC80]] | C | NDC80 activity raises CIT's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.63× lower at baseline in the lines without NDC80 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CIT's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without AURKB | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CIT's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without PBK | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises CIT's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 3.09× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDCA3]] | C | CDCA3 activity raises CIT's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without CDCA3 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25C]] | C | CIT's natural level strengthens CDC25C's drug response | CIT's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.28; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.936). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.7, -54.4); signed map (-47.7, -41.8). **Vector** length 170, 65.7% of its response variance represented; |z| ≥ 3 in 1,615 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.82 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.79 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.76 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +7.6 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | +2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.0 | +5.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.8 | +6.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +1.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +2.4 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -9.5 | -11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.3 | -15.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -9.2 | -16.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -14.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -8.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.5 | -7.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | citron rho-interacting serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:119,685,791-119,877,320 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0949, STK21, CRIK, CITK |
| Gene groups (HGNC) | MicroRNA protein coding host genes; DMPK kinase family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 9 pathways, smallest: RHO GTPases activate CIT; RHOB GTPase cycle; RHOC GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O14578](https://www.uniprot.org/uniprotkb/O14578) (Citron Rho-interacting kinase):

> Plays a role in cytokinesis. Required for KIF14 localization to the central spindle and midbody. Putative RHO/RAC effector that binds to the GTP-bound forms of RHO and RAC1. It probably binds p21 with a tighter specificity in vivo. Displays serine/threonine protein kinase activity. Plays an important role in the regulation of cytokinesis and the development of the central nervous system. Phosphorylates MYL9/MLC2.

**Summary**, from NCBI Gene [11113](https://www.ncbi.nlm.nih.gov/gene/11113):

> This gene encodes a serine/threonine-protein kinase that functions in cell division. Together with the kinesin KIF14, this protein localizes to the central spindle and midbody, and functions to promote efficient cytokinesis. This protein is involved in central nervous system development. Polymorphisms in this gene are associated with bipolar disorder and risk for schizophrenia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:1985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1985) · Entrez [11113](https://www.ncbi.nlm.nih.gov/gene/11113) · UniProt [O14578](https://www.uniprot.org/uniprotkb/O14578) · Ensembl [ENSG00000122966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122966)

## Data

Gene col 4390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4390); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4390]; `tensor/DDL_lfc|DDL_z.npy` [4390]; `embed/gene_vectors.npy` [4390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4390 or target_col == 4390). Every well: [[CIT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
