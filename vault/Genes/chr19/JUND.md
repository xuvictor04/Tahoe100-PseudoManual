---
symbol: "JUND"
type: "gene"
col: 5077
ensembl_id: "ENSG00000130522"
name: "JunD proto-oncogene, AP-1 transcription factor subunit"
location: "19p13.11"
module: 123
arm: "+"
pooled_cpm: 35.83
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# JUND

*JunD proto-oncogene, AP-1 transcription factor subunit* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.53× (z +13.5, q 2e-38, up in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.09× (z +4.5, q 7e-04, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.434× (z -7.4, q 6e-11, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SNU-423 0.200×, MIA PaCa-2 0.232×, NCI-H460 0.267×, CFPAC-1 0.323×, …); [[Selinexor (drug)]] 5 µM in 2 lines (HS-578T 0.167×, A-427 0.331×; ⚠ cell-cycle shift, explains ~63% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (AN3 CA 0.0605×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOB]] (+0.77, fdr 7e-06), [[DUSP8]] (+0.74, fdr 7e-06), [[KLF2]] (+0.73, fdr 7e-06); moves opposite to [[GMPS]] (-0.65, fdr 7e-06), [[RNPS1]] (-0.64, fdr 7e-06), [[NUP205]] (-0.62, fdr 7e-06).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **4.53×** | +13.5 | 2e-38 | 44/47 (A498, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.47×** | +7.5 | 1e-11 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.26×** | +5.1 | 6e-05 | 33/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +4.5 | 7e-04 | 34/45 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.09×** | +4.5 | 7e-04 | 28/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.8 | 0.012 | 31/47 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.36×** | +3.8 | 0.012 | 40/47 (BT-474, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.84×** | +3.7 | 0.017 | 32/47 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +3.6 | 0.017 | 21/38 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.017 | 35/48 (A498, HEC-1-A, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.74×** | +3.5 | 0.024 | 31/47 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **2.20×** | +3.5 | 0.024 | 37/48 (SK-MEL-2, C32, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +3.3 | 0.043 | 11/49 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.08×** | +3.2 | 0.045 | 36/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.08×** | +3.2 | 0.045 | 36/48 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.06×** | +3.2 | 0.049 | 37/46 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.058 | 31/47 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.081 | 25/48 (C32, A-172, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.59×** | +2.9 | 0.095 | 24/47 (SK-MEL-2, SW1417, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.93×** | +2.9 | 0.095 | 35/48 (A-427, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5077.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SNU-423 0.200×, MIA PaCa-2 0.232×, NCI-H460 0.267×, CFPAC-1 0.323×, …); [[Selinexor (drug)]] 5 µM in 2 lines (HS-578T 0.167×, A-427 0.331×; ⚠ cell-cycle shift, explains ~63% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (AN3 CA 0.0605×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -7.4 | 6e-11 | 43/48 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.628×** | -4.1 | 0.010 | 30/48 (HS-578T, A-427, …) | top dose only | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.665×** | -3.6 | 0.050 | 39/48 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.670×** | -3.6 | 0.050 | 34/48 (CHP-212, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.585× | -3.2 | 0.12 | 28/47 (SNU-423, SW48, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.599× | -3.2 | 0.12 | 41/48 (LoVo, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.605× | -3.2 | 0.13 | 36/48 (NCI-H460, HS-578T, …) | top dose only | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.713× | -3.0 | 0.18 | 31/48 (COLO 205, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.1 | 8 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +15.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 9.17× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 49.3 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +11.6) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -10.3) |
| [[A498 (line)]] | wt | 30.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +18.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 65.4 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +13.9) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -9.3) |
| [[HS-578T (line)]] | alt | 39.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +12.5) ⚠ cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.167× (z -13.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H1573 (line)]] | alt | 18.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +14.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 31.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +16.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 56.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.5) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -9.3) |
| [[LS 180 (line)]] | wt | 62.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +11.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 17.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +12.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 63.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +11.1) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -12.9) |
| [[A-172 (line)]] | wt | 57.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +13.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.331× (z -8.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0605× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +13.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 44.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +9.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +12.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 67.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +10.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +12.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 46.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.37× (z +15.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +13.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 42.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +12.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +10.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 37.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 46.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +9.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +11.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +8.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +11.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +10.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOB]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[DUSP8]] | +0.74 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[KLF2]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 | STRING 482 |
| [[PIM3]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TUBB2B]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[ATF4]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 | STRING 553 |
| [[KRTAP5-AS1]] | +0.65 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[BBC3]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[UBE2B]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HES4]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DAAM1]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MTHFR]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMPS]] | -0.65 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[RNPS1]] | -0.64 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[NUP205]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[NSUN2]] | -0.61 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[DPAGT1]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZCCHC4]] | -0.60 | -0.40 / -0.69 | both halves | 5e-05 |  |
| [[CUL2]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[NAA50]] | -0.60 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[PTGFRN]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ELAVL1]] | -0.59 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[SUV39H2]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RNF4]] | -0.59 | -0.65 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -0.6); signed map (-0.5, 22.4). **Vector** length 140, 52.9% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +10.4 | +13.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.2 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.2 | +5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.4 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.0 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.9 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.7 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -2.8 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | JunD proto-oncogene, AP-1 transcription factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,279,694-18,281,622 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AP-1 |
| Gene groups (HGNC) | Jun transcription factor family |
| Reactome | 16 pathways, smallest: NGF-stimulated transcription; Regulation of PD-L1(CD274) transcription; Nuclear Events (kinase and transcription factor activation) |
| Matched by | ensembl_id |

**Function**, from UniProt [P17535](https://www.uniprot.org/uniprotkb/P17535) (Transcription factor JunD):

> Transcription factor binding AP-1 sites. Heterodimerizes with proteins of the FOS family to form an AP-1 transcription factor complex, thereby enhancing their DNA binding activity to an AP-1 consensus sequence 3'-TGA[GC]TCA-5' and enhancing their transcriptional activity.

**Summary**, from NCBI Gene [3727](https://www.ncbi.nlm.nih.gov/gene/3727):

> The protein encoded by this intronless gene is a member of the JUN family, and a functional component of the AP1 transcription factor complex. This protein has been proposed to protect cells from p53-dependent senescence and apoptosis. Alternative translation initiation site usage results in the production of different isoforms (PMID:12105216). [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:6206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6206) · Entrez [3727](https://www.ncbi.nlm.nih.gov/gene/3727) · UniProt [P17535](https://www.uniprot.org/uniprotkb/P17535) · Ensembl [ENSG00000130522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130522)

## Data

Gene col 5077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5077); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5077]; `tensor/DDL_lfc|DDL_z.npy` [5077]; `embed/gene_vectors.npy` [5077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5077 or target_col == 5077). Every well: [[JUND — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JUND.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
