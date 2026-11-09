---
symbol: "USP53"
type: "gene"
col: 6987
ensembl_id: "ENSG00000145390"
name: "ubiquitin specific peptidase 53"
location: "4q26"
module: 31
arm: "+"
pooled_cpm: 201.31
n_lines_expressing: 46
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# USP53

*ubiquitin specific peptidase 53* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +13.3, q 2e-37, up in 36 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.424× (z -15.3, q 0e+00, down in 36 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.721× (z -8.6, q 1e-15, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2D1]] (+0.58, fdr 1e-05), [[KLF5]] (+0.57, fdr 1e-05), [[NCOA3]] (+0.57, fdr 1e-05); moves opposite to [[SMPD4]] (-0.60, fdr 2e-05), [[ELAVL1]] (-0.57, fdr 1e-05), [[NDUFA10]] (-0.57, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KLF5]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Homoharringtonine (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +13.3 | 2e-37 | 36/44 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +9.6 | 3e-19 | 33/44 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +8.7 | 9e-16 | 36/44 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +8.1 | 1e-13 | 39/44 (RPMI-7951, RKO, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +7.9 | 3e-13 | 35/45 (HT-29, CHP-212, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +7.5 | 7e-12 | 33/44 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +7.4 | 9e-12 | 32/44 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.46×** | +7.0 | 2e-10 | 34/44 (HT-29, CHP-212, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 4e-08 | 37/45 (RPMI-7951, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +6.1 | 8e-08 | 32/43 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 9e-07 | 26/44 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 2e-06 | 29/44 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +5.2 | 8e-06 | 26/43 (COLO 205, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 2e-05 | 27/44 (HT-29, CHP-212, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +4.5 | 2e-04 | 25/43 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.5 | 2e-04 | 22/44 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 7e-04 | 22/44 (A498, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -15.3 | 0e+00 | 36/40 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.488×** | -13.3 | 6e-38 | 40/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.498×** | -11.9 | 1e-30 | 37/41 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -8.6 | 1e-15 | 27/45 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.854× | -4.1 | 0.004 | 14/44 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.813×** | -3.8 | 0.012 | 23/44 (BT-474, NCI-H1573, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.812×** | -3.7 | 0.016 | 20/44 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | **0.820×** | -3.7 | 0.016 | 21/44 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.839× | -3.3 | 0.071 | 18/44 (HOP62, J82, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.847× | -3.1 | 0.099 | 14/43 (NCI-H661, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.843× | -3.1 | 0.099 | 21/43 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.890× | -3.1 | 0.099 | 12/44 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.848× | -3.1 | 0.099 | 20/44 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.10 | 19/43 (C32, CHP-212, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 298 | 9 (2 ⚠) | 4 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.23× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -13.4) |
| [[SW1417 (line)]] | alt | 194 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -12.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 307 | 6 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.413× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~17% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.441× (z -8.5) |
| [[LoVo (line)]] | wt | 339 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 279 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 359 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +22.9) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -14.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 259 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.4) | [[Cobimetinib (drug)]] 0.5 µM 0.353× (z -11.2) |
| [[A498 (line)]] | wt | 144 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +17.9) | — |
| [[BT-474 (line)]] | alt | 329 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -11.5) |
| [[KATO III (line)]] | alt | 205 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 343 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -10.6) |
| [[A-427 (line)]] | wt | 347 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -12.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 255 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -19.8) |
| [[CFPAC-1 (line)]] | alt | 369 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.1) |
| [[CHP-212 (line)]] | wt | 118 | 3 (1 ⚠) | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 4.47× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 180 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +15.3) | [[Lonafarnib (drug)]] 5 µM 0.0909× (z -14.6) ⚠ toxic |
| [[RKO (line)]] | wt | 133 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 223 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -13.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 153 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 170 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.8) | — |
| [[LS 180 (line)]] | wt | 344 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 207 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 122 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.4) |
| [[PANC-1 (line)]] | alt | 55.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 98.9 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.34× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 261 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.5) |
| [[SW48 (line)]] | wt | 218 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 96.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 193 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -10.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 129 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.0) | — |
| [[J82 (line)]] | alt | 133 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 510 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 199 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 174 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 179 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 68.7 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.93× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0639× (z -14.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.407× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.3) | — |
| [[AN3 CA (line)]] | alt | 36.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 113 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2D1]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[KLF5]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NCOA3]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PPP1R21]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CDKN2B]] | +0.55 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[ABI1]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[UBAP1]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[GK]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.53 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[MYO1D]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SDR16C5]] | +0.52 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[AMN1]] | +0.51 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPD4]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ELAVL1]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[NDUFA10]] | -0.57 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[TMX2]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[DNAAF5]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[HSPA14]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MFN2]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ILF3]] | -0.47 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[FARS2]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CNOT9]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[RANBP3]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[COPS3]] | -0.47 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF5]] | B | KLF5 activity raises USP53's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without KLF5 | 0.003 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[FAM83B]] | B | FAM83B activity raises USP53's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without FAM83B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[RNF223]] | B | RNF223 activity raises USP53's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without RNF223 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[IL18]] | B | IL18 activity raises USP53's level | lines that do not express IL18 (18) vs lines expressing it (32) | 2.09× lower at baseline in the lines without IL18 | 0.018 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3 |
| [[LIPH]] | B | LIPH activity raises USP53's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without LIPH | 0.021 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[DAPP1]] | B | DAPP1 activity raises USP53's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 2.15× lower at baseline in the lines without DAPP1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[CYP3A5]] | B | CYP3A5 activity raises USP53's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 1.53× lower at baseline in the lines without CYP3A5 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[SDR16C5]] | B | SDR16C5 activity raises USP53's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without SDR16C5 | 0.047 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[CD55]] | B | CD55 activity raises USP53's level | lines that do not express CD55 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without CD55 | 0.073 | ⚠ within organs, on part of the lines; also absent: IL32, IL2RG, ENSG00000271933; maybe low, not absent |
| [[MYO1D]] | B | MYO1D activity raises USP53's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without MYO1D | 0.089 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | USP53 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express USP53 (4) vs lines expressing it (44) | the lines without USP53: 0.55× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: MORC4, SVIP, PLEKHA5; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | C | USP53 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express USP53 (4) vs lines expressing it (44) | the lines without USP53: 0.22× the cells of the other lines | 0.030 | ⚠ few lines (4 vs 46); across organs; also absent: MORC4, SVIP, PLEKHA5; maybe low, not absent |
| [[FAM241A]] | C | USP53 activity raises FAM241A's level | lines that do not express USP53 (4) vs lines expressing it (46) | 3.24× lower at baseline in the lines without USP53 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: MORC4, SVIP, PLEKHA5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.380). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.9, -33.0); signed map (6.0, 20.6). **Vector** length 116, 38.9% of its response variance represented; |z| ≥ 3 in 1,443 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.4 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.9 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.9 | +7.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.3 | +7.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.1 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.2 | +5.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.2 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.8 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.1 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -8.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.4 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 53 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:119,212,587-119,295,518 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1350 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70EK8](https://www.uniprot.org/uniprotkb/Q70EK8) (Ubiquitin carboxyl-terminal hydrolase 53):

> Deubiquitinase that mediates 'Lys-63'-linked deubiquitination of tight junction proteins, such as MARVELD2 and LSR, and which is involved in the survival of auditory hair cells and hearing. Specifically cleaves 'Lys-63'-linked polyubiquitin chains composed of at least 3 ubiquitin molecules, while it is not able to deubiquitinate substrates with shorter ubiquitin chains: recognizes ubiquitin chain in position S2 and catalyzes en bloc cleavage of polyubiquitin chains from substrate proteins. …

**Summary**, from NCBI Gene [54532](https://www.ncbi.nlm.nih.gov/gene/54532):

> Enables K63-linked deubiquitinase activity. Predicted to be involved in response to auditory stimulus and sensory perception of sound. Predicted to act upstream of or within action potential and neuron apoptotic process. Located in bicellular tight junction. Implicated in progressive familial intrahepatic cholestasis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29255) · Entrez [54532](https://www.ncbi.nlm.nih.gov/gene/54532) · UniProt [Q70EK8](https://www.uniprot.org/uniprotkb/Q70EK8) · Ensembl [ENSG00000145390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145390)

## Data

Gene col 6987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6987); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6987]; `tensor/DDL_lfc|DDL_z.npy` [6987]; `embed/gene_vectors.npy` [6987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6987 or target_col == 6987). Every well: [[USP53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
