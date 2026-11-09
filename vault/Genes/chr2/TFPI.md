---
symbol: "TFPI"
type: "gene"
col: 35
ensembl_id: "ENSG00000003436"
name: "tissue factor pathway inhibitor"
location: "2q32.1"
module: 147
arm: "+"
pooled_cpm: 274.52
n_lines_expressing: 36
n_dd_up: 2
n_dd_down: 40
n_dd_up_clean: 1
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# TFPI

*tissue factor pathway inhibitor* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 1.29× (z +3.9, q 0.059, up in 18 of 33 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[BAY1125976 (drug)]] 5 µM: 1.60× (z +3.7, q 0.059, up in 22 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 3 lines (A-427 1.84×, LS 180 1.95×, COLO 205 2.00×); [[Daptomycin (drug)]] 0.5 µM in 2 lines (COLO 205 3.44×, A-427 2.27×; ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM in 2 lines (COLO 205 3.58×, SHP-77 3.48×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 1.81×).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.134× (z -30.3, q 0e+00, down in 34 of 34 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLIS3]] (+0.65, fdr 7e-06), [[ZNF281]] (+0.57, fdr 2e-05), [[PAPPA]] (+0.55, fdr 1e-05); moves opposite to [[PIK3C2B]] (-0.55, fdr 1e-05), [[BMP7]] (-0.55, fdr 1e-05), [[TPD52]] (-0.53, fdr 8e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PAPPA]] → it (grade B ⚠); 5 go from it, the strongest it → [[TANK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 35.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 3 lines (A-427 1.84×, LS 180 1.95×, COLO 205 2.00×); [[Daptomycin (drug)]] 0.5 µM in 2 lines (COLO 205 3.44×, A-427 2.27×; ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM in 2 lines (COLO 205 3.58×, SHP-77 3.48×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 1.81×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +3.9 | 0.059 | 18/33 (COLO 205, A-427, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.059 | 22/34 (MIA PaCa-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.26× | +3.4 | 0.13 | 17/33 (COLO 205, SHP-77, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.24× | +3.3 | 0.13 | 17/34 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 1.50× | +3.2 | 0.13 | 15/35 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.23× | +3.2 | 0.13 | 16/34 (COLO 205, SHP-77, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.14 | 16/35 (RKO, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.18 | 16/34 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 35.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.134×** | -30.3 | 0e+00 | 34/34 (NCI-H1792, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.173×** | -26.4 | 0e+00 | 34/34 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.176×** | -26.2 | 0e+00 | 34/34 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.354×** | -22.1 | 0e+00 | 34/35 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.367×** | -15.1 | 0e+00 | 33/34 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.452×** | -11.9 | 7e-31 | 32/34 (SW 900, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.254×** | -10.8 | 3e-25 | 31/34 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.286×** | -9.8 | 5e-21 | 31/34 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.315×** | -9.1 | 5e-18 | 28/34 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.657×** | -8.9 | 2e-17 | 22/34 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.542×** | -8.9 | 4e-17 | 31/34 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.332×** | -8.7 | 2e-16 | 33/35 (A-172, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.343×** | -8.4 | 1e-15 | 27/34 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.583×** | -7.8 | 2e-13 | 27/33 (hTERT-HPNE, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.372×** | -7.8 | 2e-13 | 32/34 (NCI-H1792, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.605×** | -7.6 | 1e-12 | 30/34 (CHP-212, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.719×** | -7.0 | 9e-11 | 27/34 (RKO, SHP-77, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.629×** | -7.0 | 1e-10 | 24/34 (A-427, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 35. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 691 | 0 | 18 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0595× (z -29.3) |
| [[NCI-H460 (line)]] | wt | 464 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -23.6) |
| [[hTERT-HPNE (line)]] | wt | 736 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -20.2) |
| [[RKO (line)]] | wt | 390 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0822× (z -28.0) |
| [[COLO 205 (line)]] | alt | 115 | 6 (2 ⚠) | 4 | [[Daptomycin (drug)]] 0.5 µM 3.44× (z +11.0) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 3.58× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.0811× (z -22.3) |
| [[A-172 (line)]] | wt | 679 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -18.8) |
| [[A-427 (line)]] | wt | 516 | 7 (4 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 2.93× (z +12.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.84× (z +10.1) | [[Ponatinib (drug)]] 5 µM 0.429× (z -9.8) |
| [[A498 (line)]] | wt | 717 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -17.4) |
| [[A549 (line)]] | wt | 615 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0960× (z -24.0) |
| [[H4 (line)]] | wt | 331 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0506× (z -28.0) |
| [[HS-578T (line)]] | alt | 659 | 0 | 8 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -14.6) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -13.2) |
| [[HT-29 (line)]] | alt | 197 | 1 (1 ⚠) | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.0966× (z -25.9) |
| [[SHP-77 (line)]] | alt | 103 | 3 (1 ⚠) | 5 | [[Daptomycin (drug)]] 5 µM 3.50× (z +10.2) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 3.48× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.9) |
| [[SW 900 (line)]] | alt | 430 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -18.8) |
| [[CHP-212 (line)]] | wt | 222 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -15.3) |
| [[LS 180 (line)]] | wt | 78.7 | 3 (2 ⚠) | 4 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.95× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -17.7) |
| [[Panc 03.27 (line)]] | alt | 163 | 1 | 6 (1 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.23× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.101× (z -24.7) |
| [[HEC-1-A (line)]] | alt | 113 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -13.8) |
| [[HOP62 (line)]] | alt | 253 | 1 (1 ⚠) | 5 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.15× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | [[Panobinostat (drug)]] 5 µM 0.107× (z -26.5) |
| [[Hs 766T (line)]] | wt | 103 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -17.4) |
| [[J82 (line)]] | alt | 349 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.100× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 257 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 292 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 428 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -21.9) |
| [[HepG2_C3A (line)]] | wt | 524 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 227 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -21.4) |
| [[SK-MEL-2 (line)]] | alt | 84.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -14.5) |
| [[SNU-423 (line)]] | alt | 499 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0891× (z -19.2) |
| [[SW 1088 (line)]] | alt | 592 | 0 | 5 | — | [[Decitabine (drug)]] 0.5 µM 0.0312× (z -17.2) |
| [[PANC-1 (line)]] | alt | 184 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0919× (z -18.8) |
| [[RPMI-7951 (line)]] | alt | 132 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -15.8) |
| [[MIA PaCa-2 (line)]] | alt | 367 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 453 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -10.0) |
| [[AN3 CA (line)]] | alt | 35.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 33.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 43.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 35.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 20.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 20.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 35), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIS3]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ZNF281]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PAPPA]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[OSMR]] | +0.54 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[ERCC6]] | +0.53 | +0.42 / +0.48 | both halves | 4e-05 | STRING 470 |
| [[FOXL1]] | +0.53 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[MIR100HG]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CLMP]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 | STRING 789 |
| [[TUT7]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TMEM156]] | +0.53 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[TANK]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ZBTB38]] | +0.51 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3C2B]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[BMP7]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TPD52]] | -0.53 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[GPI]] | -0.50 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[FAM102A]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PDK1]] | -0.46 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[RASAL1]] | -0.45 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[ESRP1]] | -0.45 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[CDS1]] | -0.44 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[SREBF1]] | -0.44 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[GARS1]] | -0.44 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[TENT4A]] | -0.44 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[GPT2]] | -0.44 | -0.27 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPPA]] | B | PAPPA activity raises TFPI's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.87× lower at baseline in the lines without PAPPA | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[CDS1]] | B | CDS1 activity lowers TFPI's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.96× higher at baseline in the lines without CDS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[AADAC]] | B | AADAC activity raises TFPI's level | lines that do not express AADAC (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without AADAC | 0.099 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[GLIS3]] | C | GLIS3 activity raises TFPI's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 4.18× lower at baseline in the lines without GLIS3 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TANK]] | B | TFPI activity raises TANK's level | lines that do not express TFPI (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without TFPI | 0.040 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL |
| [[AGAP3]] | B | TFPI activity lowers AGAP3's level | lines that do not express TFPI (14) vs lines expressing it (36) | 1.51× higher at baseline in the lines without TFPI | 0.086 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL |
| [[PAPPA]] | B | TFPI activity raises PAPPA's level | lines that do not express TFPI (14) vs lines expressing it (36) | 3.60× lower at baseline in the lines without TFPI | 0.089 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL |
| [[WDR45B]] | B | TFPI activity raises WDR45B's level | lines that do not express TFPI (14) vs lines expressing it (36) | 1.17× lower at baseline in the lines without TFPI | 0.096 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL |
| [[GLIS3]] | C | TFPI activity raises GLIS3's level | lines that do not express TFPI (14) vs lines expressing it (36) | 4.83× lower at baseline in the lines without TFPI | 0.014 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL; co-absent with the target |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, 8.5); signed map (10.5, 25.1). **Vector** length 123, 40.1% of its response variance represented; |z| ≥ 3 in 1,623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.5 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.2 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.9 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | -0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.3 | -15.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.1 | -10.8 |
|  | [[EX229 (drug)]] 5 µM |  | -5.6 | -8.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.4 | -9.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.3 | -7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.3 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | tissue factor pathway inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:187,464,230-187,565,760 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPI, TFI, TFPI1; previously LACI |
| Hallmark sets | UV_RESPONSE_DN, KRAS_SIGNALING_UP |
| Reactome | 4 pathways, smallest: Initiation of coagulation cascade; Regulation of clotting cascade; Coagulation pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P10646](https://www.uniprot.org/uniprotkb/P10646) (Tissue factor pathway inhibitor):

> Inhibits factor X (X(a)) directly and, in a Xa-dependent way, inhibits VIIa/tissue factor activity, presumably by forming a quaternary Xa/LACI/VIIa/TF complex. It possesses an antithrombotic action and also the ability to associate with lipoproteins in plasma.

**Summary**, from NCBI Gene [7035](https://www.ncbi.nlm.nih.gov/gene/7035):

> This gene encodes a Kunitz-type serine protease inhibitor that regulates the tissue factor (TF)-dependent pathway of blood coagulation. The coagulation process initiates with the formation of a factor VIIa-TF complex, which proteolytically activates additional proteases (factors IX and X) and ultimately leads to the formation of a fibrin clot. The product of this gene inhibits the activated factor X and VIIa-TF proteases in an autoregulatory loop. Inhibition of the encoded protein restores …

**Accessions** — [HGNC:11760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11760) · Entrez [7035](https://www.ncbi.nlm.nih.gov/gene/7035) · UniProt [P10646](https://www.uniprot.org/uniprotkb/P10646) · Ensembl [ENSG00000003436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003436)

## Data

Gene col 35: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 35); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 35, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 35]; `tensor/DDL_lfc|DDL_z.npy` [35]; `embed/gene_vectors.npy` [35]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 35 or target_col == 35). Every well: [[TFPI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFPI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
