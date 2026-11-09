---
symbol: "ACTN1"
type: "gene"
col: 1004
ensembl_id: "ENSG00000072110"
name: "actinin alpha 1"
location: "14q24.1"
module: 78
arm: "+"
pooled_cpm: 266.33
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 41
n_dd_up_clean: 2
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 22
direction_downstream: 1
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ACTN1

*actinin alpha 1* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.65× (z +9.0, q 2e-16, up in 39 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.24× (z +3.7, q 0.023, up in 25 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (A549 2.42×, A498 2.30×, SNU-423 2.70×, A-427 2.69×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 2.27×, SNU-423 2.63×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 2.46×, A498 1.92×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (A549 1.86×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.48×).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.564× (z -14.4, q 2e-44, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK3]] (+0.74, fdr 7e-06), [[ARPC2]] (+0.74, fdr 7e-06), [[SPRY4]] (+0.73, fdr 7e-06); moves opposite to [[MBIP]] (-0.60, fdr 2e-05), [[LINC02256]] (-0.60, fdr 1e-05), [[THAP3]] (-0.59, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[BCAR3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BLZF2P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1004.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (A549 2.42×, A498 2.30×, SNU-423 2.70×, A-427 2.69×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 2.27×, SNU-423 2.63×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 2.46×, A498 1.92×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (A549 1.86×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.48×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.0 | 2e-16 | 39/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.0 | 2e-13 | 30/43 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +4.5 | 0.001 | 29/44 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +3.9 | 0.013 | 23/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.023 | 25/46 (NCI-H1573, NCI-H23, …) | all doses, flat | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +3.4 | 0.055 | 20/46 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.060 | 23/46 (NCI-H23, NCI-H1573, …) | all doses, flat | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.14 | 25/47 (NCI-H23, NCI-H1573, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.14 | 21/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1004.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.564×** | -14.4 | 2e-44 | 35/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.500×** | -12.3 | 2e-32 | 42/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -12.0 | 1e-30 | 38/48 (HT-29, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.527×** | -11.0 | 7e-26 | 39/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.565×** | -10.2 | 4e-22 | 39/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -9.4 | 5e-19 | 41/47 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.647×** | -7.8 | 7e-13 | 38/47 (NCI-H23, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.650×** | -7.7 | 1e-12 | 33/47 (RKO, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.656×** | -7.5 | 4e-12 | 37/47 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.645×** | -7.5 | 4e-12 | 36/46 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.669×** | -7.5 | 4e-12 | 39/49 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.697×** | -6.7 | 8e-10 | 31/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.748×** | -6.4 | 9e-09 | 31/47 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.693×** | -6.3 | 2e-08 | 36/47 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.750×** | -6.1 | 3e-08 | 29/47 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.713×** | -6.0 | 7e-08 | 32/48 (C32, SK-MEL-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 490 | 0 | 29 (3 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.190× (z -23.7) |
| [[SK-MEL-2 (line)]] | alt | 367 | 0 | 22 (3 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.205× (z -20.9) |
| [[NCI-H23 (line)]] | alt | 402 | 0 | 21 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.580× (z -21.8) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.241× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 294 | 0 | 17 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.562× (z -26.7) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.445× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 187 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.1) |
| [[SW480 (line)]] | alt | 415 | 0 | 16 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -25.0) |
| [[NCI-H460 (line)]] | wt | 155 | 1 (1 ⚠) | 12 | [[Niclosamide (olamine) (drug)]] 5 µM 2.02× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~32% of this change | [[Cobimetinib (drug)]] 5 µM 0.365× (z -12.9) |
| [[H4 (line)]] | wt | 422 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.0) |
| [[LOX-IMVI (line)]] | wt | 392 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -28.1) |
| [[RKO (line)]] | wt | 353 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -23.2) |
| [[A498 (line)]] | wt | 276 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +13.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.426× (z -13.4) |
| [[A549 (line)]] | wt | 269 | 3 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 1.86× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -11.9) |
| [[Hs 766T (line)]] | wt | 281 | 0 | 7 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.345× (z -9.7) ⚠ toxic · without an alert: [[Trametinib (drug)]] 0.5 µM 0.441× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 222 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -12.0) |
| [[LoVo (line)]] | wt | 131 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.05× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -18.5) |
| [[J82 (line)]] | alt | 494 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -13.1) |
| [[A-427 (line)]] | wt | 86.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -14.9) |
| [[HOP62 (line)]] | alt | 417 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -10.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.8) |
| [[HS-578T (line)]] | alt | 295 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +10.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -10.1) |
| [[PANC-1 (line)]] | alt | 234 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.1) |
| [[C-33 A (line)]] | alt | 103 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 238 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -15.6) |
| [[KATO III (line)]] | alt | 154 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.0) |
| [[LS 180 (line)]] | wt | 87.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 166 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.5) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.454× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 525 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -19.8) |
| [[RPMI-7951 (line)]] | alt | 381 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -11.7) |
| [[SNU-423 (line)]] | alt | 358 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 219 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 151 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.360× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 391 | 0 | 2 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.375× (z -10.9) |
| [[HCT15 (line)]] | alt | 123 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.2) |
| [[HT-29 (line)]] | alt | 165 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 200 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.631× (z -8.5) |
| [[SW48 (line)]] | wt | 193 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -15.5) |
| [[BT-474 (line)]] | alt | 255 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0558× (z -16.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 73.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0806× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 248 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 341 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.202× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 314 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.9) |
| [[SW 900 (line)]] | alt | 236 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.410× (z -8.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 224 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.3) |
| [[AN3 CA (line)]] | alt | 158 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 292 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK3]] | +0.74 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[ARPC2]] | +0.74 | +0.77 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 547 |
| [[SPRY4]] | +0.73 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[COTL1]] | +0.72 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CORO1C]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 | STRING 529 |
| [[MSN]] | +0.70 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 432 |
| [[PXN]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | pathway: Cell junction organization; STRING 730 |
| [[ITGA3]] | +0.69 | +0.73 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 744 |
| [[MACF1]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[EGR3]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBIP]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[LINC02256]] | -0.60 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[THAP3]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[DNAJC27]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[PHC3]] | -0.58 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[PIGP]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[ASTE1]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ZCCHC8]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[FPGT]] | -0.57 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[ZNF766]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAR3]] | B | BCAR3 activity raises ACTN1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without BCAR3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[IL31RA]] | B | IL31RA activity raises ACTN1's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.56× lower at baseline in the lines without IL31RA | 0.004 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[ETS1]] | B | ETS1 activity raises ACTN1's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without ETS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[LTBP2]] | B | LTBP2 activity raises ACTN1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without LTBP2 | 0.009 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[GALNT18]] | B | GALNT18 activity raises ACTN1's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without GALNT18 | 0.016 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[HTR7]] | B | HTR7 activity raises ACTN1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.59× lower at baseline in the lines without HTR7 | 0.017 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[LINC02454]] | B | LINC02454 activity raises ACTN1's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 1.67× lower at baseline in the lines without LINC02454 | 0.019 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[RUNX1]] | B | RUNX1 activity raises ACTN1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.54× lower at baseline in the lines without RUNX1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[TMEM156]] | B | TMEM156 activity raises ACTN1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.22× lower at baseline in the lines without TMEM156 | 0.023 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[SHANK2]] | B | SHANK2 activity raises ACTN1's level | lines that do not express SHANK2 (15) vs lines expressing it (35) | 1.15× lower at baseline in the lines without SHANK2 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EPS8L2 |
| [[NPAS2]] | B | NPAS2 activity raises ACTN1's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without NPAS2 | 0.035 | ⚠ within organs, on part of the lines |
| [[CD59]] | B | CD59 activity raises ACTN1's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.00× lower at baseline in the lines without CD59 | 0.042 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BLZF2P]] | C | ACTN1's natural level strengthens BLZF2P's drug response | ACTN1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.66; direction not clear | 0.041 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.1, 6.2); signed map (6.7, 45.3). **Vector** length 145, 56.2% of its response variance represented; |z| ≥ 3 in 1,845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.8 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | -7.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.2 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.3 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -9.4 | -7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -9.2 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.7 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.1 | -6.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.1 | -6.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -8.0 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | actinin alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:68,874,128-68,979,440 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Actinins |
| Hallmark sets | ANDROGEN_RESPONSE, APICAL_JUNCTION |
| Reactome | 19 pathways, smallest: Regulation of cytoskeletal remodeling and cell spreading by IPP complex components; Cell-extracellular matrix interactions; Nephrin family interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P12814](https://www.uniprot.org/uniprotkb/P12814) (Alpha-actinin-1):

> F-actin cross-linking protein which is thought to anchor actin to a variety of intracellular structures. Association with IGSF8 regulates the immune synapse formation and is required for efficient T-cell activation.

**Summary**, from NCBI Gene [87](https://www.ncbi.nlm.nih.gov/gene/87):

> Alpha actinins belong to the spectrin gene superfamily which represents a diverse group of cytoskeletal proteins, including the alpha and beta spectrins and dystrophins. Alpha actinin is an actin-binding protein with multiple roles in different cell types. In nonmuscle cells, the cytoskeletal isoform is found along microfilament bundles and adherens-type junctions, where it is involved in binding actin to the membrane. In contrast, skeletal, cardiac, and smooth muscle isoforms are localized to …

**Accessions** — [HGNC:163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:163) · Entrez [87](https://www.ncbi.nlm.nih.gov/gene/87) · UniProt [P12814](https://www.uniprot.org/uniprotkb/P12814) · Ensembl [ENSG00000072110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072110)

## Data

Gene col 1004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1004); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1004]; `tensor/DDL_lfc|DDL_z.npy` [1004]; `embed/gene_vectors.npy` [1004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1004 or target_col == 1004). Every well: [[ACTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
