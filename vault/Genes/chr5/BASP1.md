---
symbol: "BASP1"
type: "gene"
col: 10751
ensembl_id: "ENSG00000176788"
name: "brain abundant membrane attached signal protein 1"
location: "5p15.1"
module: 14
arm: "+"
pooled_cpm: 241.23
n_lines_expressing: 26
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BASP1

*brain abundant membrane attached signal protein 1* — 5p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +9.4, q 2e-18, up in 18 of 24 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.77× (z +7.0, q 4e-10, up in 23 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.730× (z -4.1, q 0.017, down in 16 of 24 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.757× (z -3.6, q 0.054, down in 9 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (A549 0.174×, NCI-H460 0.238×, SNU-423 0.262×, NCI-H23 0.274×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (A549 0.247×, NCI-H1792 0.223×, NCI-H460 0.272×; ⚠ cell-cycle shift, explains ~96% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A549 0.251×, NCI-H1792 0.238×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.341×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP6]] (+0.60, fdr 7e-06), [[PLPP3]] (+0.58, fdr 1e-05), [[TNFAIP3]] (+0.56, fdr 1e-05); moves opposite to [[LIG3]] (-0.51, fdr 5e-05), [[TIMM10B]] (-0.50, fdr 3e-05), [[SMG1P6]] (-0.50, fdr 2e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IL1R1]] → it (grade C ⚠); 7 go from it, the strongest it → [[UGCG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.67×** | +9.4 | 2e-18 | 18/24 (hTERT-HPNE, HS-578T, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.7 | 4e-12 | 11/25 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +7.1 | 3e-10 | 10/22 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.77×** | +7.0 | 4e-10 | 23/25 (HOP62, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.4 | 2e-08 | 17/24 (A-427, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.54×** | +5.4 | 6e-06 | 19/24 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.7 | 2e-04 | 7/22 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 6e-04 | 16/25 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.35×** | +4.0 | 0.005 | 15/24 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.30×** | +3.4 | 0.032 | 9/24 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | 1.27× | +3.1 | 0.10 | 7/24 (Panc 03.27, A498, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10751.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (A549 0.174×, NCI-H460 0.238×, SNU-423 0.262×, NCI-H23 0.274×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (A549 0.247×, NCI-H1792 0.223×, NCI-H460 0.272×; ⚠ cell-cycle shift, explains ~96% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A549 0.251×, NCI-H1792 0.238×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.341×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -4.1 | 0.017 | 16/24 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.727×** | -4.0 | 0.017 | 19/24 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.054 | 9/23 (SW 1271, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.763×** | -3.5 | 0.059 | 13/24 (A549, NCI-H460, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.080 | 8/23 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.778×** | -3.3 | 0.099 | 11/24 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.766× | -3.2 | 0.11 | 7/24 (A-427, H4, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.785× | -3.2 | 0.11 | 15/24 (NCI-H1792, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,084 | 1 | 10 (10 ⚠) | [[TAK-901 (drug)]] 5 µM 4.07× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -24.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 696 | 1 | 8 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 5.59× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.223× (z -15.4) ⚠ cell-cycle shift, explains ~96% of this change |
| [[A549 (line)]] | wt | 1,013 | 0 | 8 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -27.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 432 | 2 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.63× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 84.6 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +19.7) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.67× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 663 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 68.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +17.8) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[SW 900 (line)]] | alt | 462 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.73× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 144 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.29× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 219 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +22.2) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[Panc 03.27 (line)]] | alt | 80.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.1× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 77.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +15.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.54× (z +9.7) | — |
| [[SW 1271 (line)]] | alt | 629 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 169 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +16.9) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[J82 (line)]] | alt | 602 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 415 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.341× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 456 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 144 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.2) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[LOX-IMVI (line)]] | wt | 200 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.8) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H1573 (line)]] | alt | 92.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 905 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 350 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.4) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[AN3 CA (line)]] | alt | 36.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 38.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 20.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 17.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP6]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[PLPP3]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TNFAIP3]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TGFB2]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ZEB2]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[UGCG]] | +0.54 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[PTPRM]] | +0.54 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[NEDD9]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[BHLHE41]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ARID5B]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[IRS2]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[RBMS3]] | +0.53 | +0.58 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIG3]] | -0.51 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[TIMM10B]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SMG1P6]] | -0.50 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[DPAGT1]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NPIPB11]] | -0.49 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[TMPRSS5]] | -0.49 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[METTL3]] | -0.49 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[NIPA2]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SELENOI]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[STX16-NPEPL1]] | -0.47 | -0.32 / -0.46 | both halves | 1e-04 |  |
| [[DDIAS]] | -0.47 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[NTAQ1]] | -0.46 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1R1]] | C | IL1R1 activity raises BASP1's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 6.38× lower at baseline in the lines without IL1R1 | 0.007 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1; co-absent with the target |
| [[RHCG]] | C | RHCG activity raises BASP1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 6.50× lower at baseline in the lines without RHCG | 0.078 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10; co-absent with the target |
| [[CYP1B1]] | C | CYP1B1 activity raises BASP1's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 4.25× lower at baseline in the lines without CYP1B1 | 0.087 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGCG]] | B | BASP1 activity raises UGCG's level | lines that do not express BASP1 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without BASP1 | 0.066 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| [[RAB13]] | B | BASP1 activity raises RAB13's level | lines that do not express BASP1 (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without BASP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | B | BASP1 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express BASP1 (24) vs lines expressing it (24) | the lines without BASP1: 0.77× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| cells under [[Arbutin (drug)]] 5 µM | B | BASP1 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express BASP1 (24) vs lines expressing it (24) | the lines without BASP1: 0.80× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | B | BASP1 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express BASP1 (24) vs lines expressing it (24) | the lines without BASP1: 0.87× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| cells under [[Sulfatinib (drug)]] 5 µM | B | BASP1 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express BASP1 (24) vs lines expressing it (24) | the lines without BASP1: 0.81× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | BASP1 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express BASP1 (24) vs lines expressing it (24) | the lines without BASP1: 0.81× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.475). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.1, 9.4); signed map (45.2, 16.2). **Vector** length 101, 32.6% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +7.6 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.7 | +5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +0.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.1 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | brain abundant membrane attached signal protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.1 — chr5:17,065,598-17,276,843 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAP-22, NAP22, CAP23, CAP-23 |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: RHOF GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

UniProt [P80723](https://www.uniprot.org/uniprotkb/P80723) carries no function annotation.

**Summary**, from NCBI Gene [10409](https://www.ncbi.nlm.nih.gov/gene/10409):

> This gene encodes a membrane bound protein with several transient phosphorylation sites and PEST motifs. Conservation of proteins with PEST sequences among different species supports their functional significance. PEST sequences typically occur in proteins with high turnover rates. Immunological characteristics of this protein are species specific. This protein also undergoes N-terminal myristoylation. Alternative splicing results in multiple transcript variants that encode the same protein. …

**Accessions** — [HGNC:957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:957) · Entrez [10409](https://www.ncbi.nlm.nih.gov/gene/10409) · UniProt [P80723](https://www.uniprot.org/uniprotkb/P80723) · Ensembl [ENSG00000176788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176788)

## Data

Gene col 10751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10751); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10751]; `tensor/DDL_lfc|DDL_z.npy` [10751]; `embed/gene_vectors.npy` [10751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10751 or target_col == 10751). Every well: [[BASP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BASP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
