---
symbol: "SPG21"
type: "gene"
col: 1625
ensembl_id: "ENSG00000090487"
name: "SPG21 abhydrolase domain containing, maspardin"
location: "15q22.31"
module: 122
arm: "+"
pooled_cpm: 37.27
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# SPG21

*SPG21 abhydrolase domain containing, maspardin* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.10× (z +17.1, q 0e+00, up in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.23× (z +6.7, q 3e-09, up in 24 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.231×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.227×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (LOX-IMVI 0.119×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM126B]] (+0.69, fdr 7e-06), [[NELFCD]] (+0.62, fdr 2e-05), [[GNS]] (+0.61, fdr 7e-06); moves opposite to [[ARID3B]] (-0.57, fdr 1e-05), [[FLNB-AS1]] (-0.55, fdr 1e-05), [[LUZP1]] (-0.54, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CIPC]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +17.1 | 0e+00 | 37/46 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +14.6 | 1e-45 | 35/41 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +7.3 | 4e-11 | 26/48 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +7.3 | 4e-11 | 25/45 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +6.7 | 3e-09 | 24/48 (A549, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +6.3 | 2e-08 | 26/46 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.9 | 9e-05 | 21/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 9e-05 | 19/48 (A549, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.48×** | +4.8 | 1e-04 | 17/48 (LS 180, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.4 | 5e-04 | 22/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 10/48 (NCI-H460, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.004 | 19/49 (J82, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | 1.18× | +3.7 | 0.009 | 15/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.16× | +3.3 | 0.035 | 19/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +3.2 | 0.057 | 9/47 (Hs 766T, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.057 | 10/47 (A-427, A549, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.062 | 3/48 (NCI-H460, RKO, …) | top dose only |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.066 | 8/48 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +3.0 | 0.076 | 14/48 (J82, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.091 | 6/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.098 | 14/48 (RPMI-7951, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1625.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.231×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.227×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (LOX-IMVI 0.119×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -4.2 | 0.017 | 14/48 (A-427, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.844× | -3.9 | 0.026 | 16/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.854× | -3.5 | 0.080 | 13/47 (SNU-423, LS 180, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.757× | -3.4 | 0.11 | 12/48 (SW 900, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.19 | 12/48 (SW 1271, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +17.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 57.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 49.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.4) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +15.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 46.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +13.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 22.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 62.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 35.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.88× (z +15.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 32.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.328× (z -8.6) ⚠ cell-cycle shift, explains ~3% of this change |
| [[SW480 (line)]] | alt | 33.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 53.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +16.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 29.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.119× (z -11.1) ⚠ toxic |
| [[LS 180 (line)]] | wt | 27.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 45.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM126B]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[NELFCD]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[GNS]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[RCBTB1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[VPS41]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[CDK4]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[GUF1]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[PFKM]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[APEX1]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ATP6V1C1]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MRRF]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3B]] | -0.57 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[FLNB-AS1]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[LUZP1]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[SEC61G]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[WNT2B]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FBXL18]] | -0.52 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[PLIN3]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[LINC02804]] | -0.52 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[SH3BGRL3]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.50 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[RABGEF1]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ADGRL1-AS1]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CIPC]] | C | CIPC's natural level weakens SPG21's drug response | CIPC's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.04; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-29.2, -16.5); signed map (-1.7, -36.7). **Vector** length 92.4, 20.1% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.1 | +7.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.0 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +4.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | -2.3 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SPG21 abhydrolase domain containing, maspardin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,963,022-64,990,310 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACP33, GL010, BM-019, MAST, ABHD21 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZD8](https://www.uniprot.org/uniprotkb/Q9NZD8) (Maspardin):

> May play a role as a negative regulatory factor in CD4-dependent T-cell activation.

**Summary**, from NCBI Gene [51324](https://www.ncbi.nlm.nih.gov/gene/51324):

> The protein encoded by this gene binds to the hydrophobic C-terminal amino acids of CD4 which are involved in repression of T cell activation. The interaction with CD4 is mediated by the noncatalytic alpha/beta hydrolase fold domain of this protein. It is thus proposed that this gene product modulates the stimulatory activity of CD4. Mutations in this gene are associated with autosomal recessive spastic paraplegia 21 (SPG21), also known as mast syndrome. Alternative splicing results in multiple …

**Accessions** — [HGNC:20373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20373) · Entrez [51324](https://www.ncbi.nlm.nih.gov/gene/51324) · UniProt [Q9NZD8](https://www.uniprot.org/uniprotkb/Q9NZD8) · Ensembl [ENSG00000090487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090487)

## Data

Gene col 1625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1625); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1625]; `tensor/DDL_lfc|DDL_z.npy` [1625]; `embed/gene_vectors.npy` [1625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1625 or target_col == 1625). Every well: [[SPG21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPG21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
