---
symbol: "RNF43"
type: "gene"
col: 2938
ensembl_id: "ENSG00000108375"
name: "ring finger protein 43"
location: "17q22"
module: 55
arm: "+"
pooled_cpm: 68.84
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 109
direction_downstream: 100
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# RNF43

*ring finger protein 43* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +7.0, q 1e-09, up in 9 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.568× (z -9.4, q 2e-18, down in 19 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AXIN2]] (+0.83, fdr 7e-06), [[TOX3]] (+0.79, fdr 7e-06), [[LINC02253]] (+0.77, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 109 arrows point to it, the strongest [[SLC44A3]] → it (grade B ⚠); 100 go from it, the strongest it → [[SLC44A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +7.0 | 1e-09 | 9/22 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +5.0 | 1e-04 | 9/23 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.8 | 3e-04 | 14/22 (BT-474, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.5 | 0.001 | 0/22 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.003 | 13/22 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.023 | 6/22 (C32, A-427, …) | top dose only | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.023 | 0/22 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.16× | +3.6 | 0.023 | 6/23 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +3.5 | 0.029 | 7/22 (LoVo, A-427, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.030 | 1/22 (SW 900) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.030 | 8/23 (AsPC-1, BT-474, …) | all doses, flat |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.030 | 5/22 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.15× | +3.4 | 0.031 | 11/22 (HT-29, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.21×** | +3.3 | 0.038 | 1/22 (AsPC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.048 | 11/22 (AsPC-1, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2938.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -9.4 | 2e-18 | 19/22 (KATO III, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -6.8 | 2e-09 | 18/22 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -6.5 | 2e-08 | 19/22 (HepG2/C3A, COLO 205, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.706×** | -5.8 | 9e-07 | 14/22 (SNU-423, CFPAC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -5.8 | 9e-07 | 18/22 (SW48, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.700×** | -5.7 | 1e-06 | 13/22 (SW 900, HT-29, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.708×** | -5.5 | 3e-06 | 8/22 (CFPAC-1, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.722×** | -5.4 | 5e-06 | 11/22 (HCT15, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.737×** | -5.1 | 3e-05 | 14/22 (SW 900, CFPAC-1, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.748×** | -4.8 | 8e-05 | 12/22 (KATO III, SW480, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.607×** | -4.3 | 7e-04 | 5/22 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.773×** | -4.3 | 9e-04 | 13/22 (LS 180, SW48, …) | two highest doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.780×** | -3.9 | 0.005 | 1/22 (NCI-H23) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.796×** | -3.8 | 0.007 | 15/22 (CFPAC-1, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.798×** | -3.7 | 0.008 | 10/22 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.800×** | -3.7 | 0.008 | 13/22 (KATO III, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.861× | -3.5 | 0.017 | 16/23 (CFPAC-1, HCT15, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.695×** | -3.2 | 0.045 | 1/23 (Panc 03.27) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 515 | 0 | 18 (15 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -26.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -13.4) |
| [[SW480 (line)]] | alt | 194 | 0 | 14 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -23.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.215× (z -14.9) |
| [[HepG2_C3A (line)]] | wt | 138 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -12.9) |
| [[SW48 (line)]] | wt | 669 | 0 | 13 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -23.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.140× (z -16.1) |
| [[COLO 205 (line)]] | alt | 357 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -11.4) |
| [[KATO III (line)]] | alt | 211 | 0 | 12 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -19.4) |
| [[LoVo (line)]] | wt | 159 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -20.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.360× (z -9.1) |
| [[HT-29 (line)]] | alt | 185 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -22.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.217× (z -13.5) |
| [[SW1417 (line)]] | alt | 292 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -22.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -9.8) |
| [[A-427 (line)]] | wt | 36.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.253× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 135 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.169× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 28.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.5) |
| [[BT-474 (line)]] | alt | 48.6 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.61× (z +9.3) | — |
| [[C32 (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.88 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AXIN2]] | +0.83 | +0.77 / +0.82 | both halves | 7e-06 | pathway: Signaling by WNT; STRING 805 |
| [[TOX3]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[LINC02253]] | +0.77 | +0.63 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[BMP4]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SORL1]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[CLRN3]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[ARHGEF38]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[PROM1]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*109 arrows, 109 of them with an alert ⚠; grade A 0, B 16, C 93. Shown: the 12 strongest; 97 more arrows (97 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | SLC44A3 activity raises RNF43's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.49× lower at baseline in the lines without SLC44A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises RNF43's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 3.08× lower at baseline in the lines without SHROOM3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[KSR2]] | B | KSR2 activity raises RNF43's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without KSR2 | 0.017 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises RNF43's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.50× lower at baseline in the lines without TJP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[SNTB1]] | B | SNTB1 activity raises RNF43's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 3.27× lower at baseline in the lines without SNTB1 | 0.035 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[ATP8B1]] | B | ATP8B1 activity raises RNF43's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.50× lower at baseline in the lines without ATP8B1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[ARSL]] | B | ARSL activity strengthens RNF43's drug response | lines that do not express ARSL (11) vs lines expressing it (11) | the lines without ARSL respond 0.57× as strongly (z diff +1.97); strongest at Homoharringtonine 0.5 µM: 0.64x vs 0.31x (z diff +4.2) | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4; target measured in part of the lines; artifact flags |
| [[RSPH1]] | B | RSPH1 activity raises RNF43's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.45× lower at baseline in the lines without RSPH1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[NCALD]] | B | NCALD activity raises RNF43's level | lines that do not express NCALD (18) vs lines expressing it (32) | 2.44× lower at baseline in the lines without NCALD | 0.076 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity raises RNF43's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 2.83× lower at baseline in the lines without LINC01876 | 0.079 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[MROH7]] | B | MROH7 activity raises RNF43's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without MROH7 | 0.082 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[RAPGEF5]] | B | RAPGEF5 activity raises RNF43's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.39× lower at baseline in the lines without RAPGEF5 | 0.084 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |

### Downstream of this gene

*100 arrows, 100 of them with an alert ⚠; grade A 0, B 23, C 77. Shown: the 12 strongest; 88 more arrows (88 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | RNF43 activity raises SLC44A3's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.18× lower at baseline in the lines without RNF43 | 1e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[PIK3C2B]] | B | RNF43 activity raises PIK3C2B's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.09× lower at baseline in the lines without RNF43 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[PLS1]] | B | RNF43 activity raises PLS1's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.15× lower at baseline in the lines without RNF43 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[MROH7]] | B | RNF43 activity raises MROH7's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.04× lower at baseline in the lines without RNF43 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[TSPOAP1-AS1]] | B | RNF43 activity raises TSPOAP1-AS1's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 1.63× lower at baseline in the lines without RNF43 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[DLG3]] | B | RNF43 activity raises DLG3's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.48× lower at baseline in the lines without RNF43 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[RSPH1]] | B | RNF43 activity raises RSPH1's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without RNF43 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[SHROOM3]] | B | RNF43 activity raises SHROOM3's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.56× lower at baseline in the lines without RNF43 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[BCL2L15]] | B | RNF43 activity raises BCL2L15's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without RNF43 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[LNX1]] | B | RNF43 activity raises LNX1's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.19× lower at baseline in the lines without RNF43 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[USP6NL]] | B | RNF43 activity raises USP6NL's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without RNF43 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[SNTB1]] | B | RNF43 activity raises SNTB1's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.26× lower at baseline in the lines without RNF43 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.9, 48.7); signed map (61.9, 11.6). **Vector** length 106, 39.5% of its response variance represented; |z| ≥ 3 in 693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.2 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Ixazomib (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,353,676-58,417,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20315, RNF124, DKFZp781H0392, URCC |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 6 pathways, smallest: Signaling by RNF43 mutants; Regulation of FZD by ubiquitination; Signaling by WNT in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DV7](https://www.uniprot.org/uniprotkb/Q68DV7) (E3 ubiquitin-protein ligase RNF43):

> E3 ubiquitin-protein ligase that acts as a negative regulator of the Wnt signaling pathway by mediating the ubiquitination, endocytosis and subsequent degradation of Wnt receptor complex components Frizzled. Acts on both canonical and non-canonical Wnt signaling pathway. Along with RSPO2 and ZNRF3, constitutes a master switch that governs limb specification (By similarity).

**Summary**, from NCBI Gene [54894](https://www.ncbi.nlm.nih.gov/gene/54894):

> The protein encoded by this gene is a RING-type E3 ubiquitin ligase and is predicted to contain a transmembrane domain, a protease-associated domain, an ectodomain, and a cytoplasmic RING domain. This protein is thought to negatively regulate Wnt signaling, and expression of this gene results in an increase in ubiquitination of frizzled receptors, an alteration in their subcellular distribution, resulting in reduced surface levels of these receptors. Mutations in this gene have been reported in …

**Accessions** — [HGNC:18505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18505) · Entrez [54894](https://www.ncbi.nlm.nih.gov/gene/54894) · UniProt [Q68DV7](https://www.uniprot.org/uniprotkb/Q68DV7) · Ensembl [ENSG00000108375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108375)

## Data

Gene col 2938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2938); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2938]; `tensor/DDL_lfc|DDL_z.npy` [2938]; `embed/gene_vectors.npy` [2938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2938 or target_col == 2938). Every well: [[RNF43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
