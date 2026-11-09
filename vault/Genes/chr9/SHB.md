---
symbol: "SHB"
type: "gene"
col: 2845
ensembl_id: "ENSG00000107338"
name: "SH2 domain containing adaptor protein B"
location: "9p13.1"
module: 81
arm: "+"
pooled_cpm: 195.3
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 46
n_dd_up_clean: 2
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 50
direction_downstream: 28
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# SHB

*SH2 domain containing adaptor protein B* — 9p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 4.53× (z +11.9, q 1e-29, up in 40 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 13 lines (HS-578T 14.8×, HEC-1-A 9.59×, NCI-H1573 14.4×, SW480 6.95×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 5.84×, Panc 03.27 2.82×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (HS-578T 8.08×, HEC-1-A 7.07×).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.385× (z -13.8, q 2e-40, down in 36 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.535× (z -9.4, q 1e-18, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHD1]] (+0.79, fdr 7e-06), [[SEMA4B]] (+0.74, fdr 7e-06), [[MAP2K3]] (+0.74, fdr 7e-06).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[ITGA3]] → it (grade B ⚠); 28 go from it, the strongest it → [[CD44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2845.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 13 lines (HS-578T 14.8×, HEC-1-A 9.59×, NCI-H1573 14.4×, SW480 6.95×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 5.84×, Panc 03.27 2.82×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (HS-578T 8.08×, HEC-1-A 7.07×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.53×** | +11.9 | 1e-29 | 40/44 (HS-578T, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +5.1 | 1e-04 | 35/43 (HS-578T, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.5 | 0.081 | 16/43 (LOX-IMVI, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -13.8 | 2e-40 | 36/39 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.463×** | -11.5 | 2e-28 | 33/44 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.535×** | -9.4 | 1e-18 | 39/44 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.582×** | -9.3 | 2e-18 | 40/43 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.534×** | -9.1 | 2e-17 | 40/43 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.580×** | -9.0 | 2e-17 | 36/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -7.7 | 8e-13 | 29/44 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -7.6 | 2e-12 | 37/42 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.612×** | -7.1 | 9e-11 | 33/42 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -7.1 | 9e-11 | 37/42 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.654×** | -6.9 | 3e-10 | 36/44 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.610×** | -6.9 | 3e-10 | 32/43 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.687×** | -6.2 | 2e-08 | 31/43 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.665×** | -6.1 | 4e-08 | 31/42 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.666×** | -6.1 | 4e-08 | 37/43 (NCI-H23, H4, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.483×** | -5.7 | 4e-07 | 36/42 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.685×** | -5.7 | 5e-07 | 28/43 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.703×** | -5.3 | 4e-06 | 28/43 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -5.2 | 5e-06 | 26/43 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 235 | 0 | 23 (6 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.548× (z -21.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.272× (z -14.6) |
| [[HOP62 (line)]] | alt | 349 | 2 | 16 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.98× (z +9.2) | [[Clobetasol propionate (drug)]] 0.5 µM 0.278× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 123 | 0 | 14 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.425× (z -28.4) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.305× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 119 | 1 (1 ⚠) | 10 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +25.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.273× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 90.3 | 1 | 10 | [[TAK-901 (drug)]] 5 µM 6.57× (z +9.9) | [[Trametinib (drug)]] 0.5 µM 0.356× (z -12.1) |
| [[SNU-423 (line)]] | alt | 277 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -12.8) |
| [[HS-578T (line)]] | alt | 327 | 3 (1 ⚠) | 5 | [[TAK-901 (drug)]] 5 µM 14.8× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -19.7) |
| [[LS 180 (line)]] | wt | 238 | 0 | 8 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.289× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 83.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.364× (z -10.2) |
| [[SW480 (line)]] | alt | 175 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.95× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.474× (z -11.3) |
| [[A498 (line)]] | wt | 297 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.1) |
| [[A549 (line)]] | wt | 397 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.66× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -12.9) |
| [[H4 (line)]] | wt | 242 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +9.7) | [[Ponatinib (drug)]] 5 µM 0.277× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 239 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.59× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 209 | 2 (1 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 14.4× (z +13.8) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.274× (z -12.4) |
| [[HCT15 (line)]] | alt | 220 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.313× (z -9.8) |
| [[KATO III (line)]] | alt | 331 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 236 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.5) |
| [[BT-474 (line)]] | alt | 209 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.9) |
| [[LoVo (line)]] | wt | 159 | 0 | 4 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.331× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 235 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.49× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -18.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 219 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.46× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 138 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 11.8× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.9) |
| [[SW 900 (line)]] | alt | 348 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -13.5) |
| [[SW1417 (line)]] | alt | 263 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 208 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.24× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -15.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 171 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.55× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.280× (z -11.0) |
| [[J82 (line)]] | alt | 174 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.05× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 130 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.89× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 112 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.34× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.8) |
| [[A-172 (line)]] | wt | 197 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.79× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -14.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 189 | 0 | 2 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.232× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 279 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.419× (z -8.5) |
| [[Hs 766T (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 351 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.179× (z -8.7) |
| [[SW 1271 (line)]] | alt | 171 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.158× (z -9.1) |
| [[A-427 (line)]] | wt | 39.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 38.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 422 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD1]] | +0.79 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SEMA4B]] | +0.74 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[MAP2K3]] | +0.74 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.71 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[ARL4C]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SLC25A51]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 | ⚠ same locus (11.5 kb, same strand: neighbours can correlate without regulation) |
| [[ITGA2]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SLCO4A1]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[SYNJ2]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[DUSP5]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[IER3]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 40, C 10. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA3]] | B | ITGA3 activity raises SHB's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.65× lower at baseline in the lines without ITGA3 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises SHB's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 3.20× lower at baseline in the lines without SMAD3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[VDR]] | B | VDR activity raises SHB's level | lines that do not express VDR (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without VDR | 0.005 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[SOX9]] | B | SOX9 activity raises SHB's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without SOX9 | 0.005 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises SHB's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without EVA1A-AS | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[RAC2]] | B | RAC2 activity raises SHB's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without RAC2 | 0.010 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[HRH1]] | B | HRH1 activity raises SHB's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without HRH1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[IL1A]] | B | IL1A activity raises SHB's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without IL1A | 0.012 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[CXCL8]] | B | CXCL8 activity raises SHB's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without CXCL8 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[CD82]] | B | CD82 activity raises SHB's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without CD82 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[PLAUR]] | B | PLAUR activity raises SHB's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without PLAUR | 0.012 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises SHB's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.50× lower at baseline in the lines without ITGA2 | 0.017 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 25, C 3. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD44]] | B | SHB activity raises CD44's level | lines that do not express SHB (5) vs lines expressing it (45) | 5.84× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[CXCL8]] | B | SHB activity raises CXCL8's level | lines that do not express SHB (5) vs lines expressing it (45) | 5.77× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[PLAUR]] | B | SHB activity raises PLAUR's level | lines that do not express SHB (5) vs lines expressing it (45) | 5.52× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[PLEK2]] | B | SHB activity raises PLEK2's level | lines that do not express SHB (5) vs lines expressing it (45) | 5.35× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[RAC2]] | B | SHB activity raises RAC2's level | lines that do not express SHB (5) vs lines expressing it (45) | 4.69× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[SLCO4A1]] | B | SHB activity raises SLCO4A1's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.92× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[SMAD3]] | B | SHB activity raises SMAD3's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.89× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[LDLR]] | B | SHB activity raises LDLR's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.83× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[LUCAT1]] | B | SHB activity raises LUCAT1's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.62× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[PMEPA1]] | B | SHB activity raises PMEPA1's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.58× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[LINC00887]] | B | SHB activity raises LINC00887's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.06× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[MARCHF3]] | B | SHB activity raises MARCHF3's level | lines that do not express SHB (5) vs lines expressing it (45) | 2.41× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.3, 2.1); signed map (3.1, 44.5). **Vector** length 150, 56.3% of its response variance represented; |z| ≥ 3 in 1,874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.5 | +11.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +5.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +3.0 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +0.9 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -10.2 | -9.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -9.8 | -9.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -9.2 | -9.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.8 | -9.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.4 | -7.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.1 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | SH2 domain containing adaptor protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.1 — chr9:37,915,898-38,069,227 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing |
| Reactome | 3 pathways, smallest: VEGFA-VEGFR2 Pathway; Signaling by VEGF; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15464](https://www.uniprot.org/uniprotkb/Q15464) (SH2 domain-containing adapter protein B):

> Adapter protein which regulates several signal transduction cascades by linking activated receptors to downstream signaling components. May play a role in angiogenesis by regulating FGFR1, VEGFR2 and PDGFR signaling. May also play a role in T-cell antigen receptor/TCR signaling, interleukin-2 signaling, apoptosis and neuronal cells differentiation by mediating basic-FGF and NGF-induced signaling cascades. May also regulate IRS1 and IRS2 signaling in insulin-producing cells.

**Summary**, from NCBI Gene [6461](https://www.ncbi.nlm.nih.gov/gene/6461):

> Enables phosphotyrosine residue binding activity. Predicted to be involved in signal transduction. Predicted to act upstream of or within several processes, including hematopoietic stem cell proliferation; negative regulation of oocyte maturation; and positive regulation of immune response. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10838) · Entrez [6461](https://www.ncbi.nlm.nih.gov/gene/6461) · UniProt [Q15464](https://www.uniprot.org/uniprotkb/Q15464) · Ensembl [ENSG00000107338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107338)

## Data

Gene col 2845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2845); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2845]; `tensor/DDL_lfc|DDL_z.npy` [2845]; `embed/gene_vectors.npy` [2845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2845 or target_col == 2845). Every well: [[SHB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
