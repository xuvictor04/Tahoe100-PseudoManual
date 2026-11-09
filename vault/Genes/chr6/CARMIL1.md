---
symbol: "CARMIL1"
type: "gene"
col: 1262
ensembl_id: "ENSG00000079691"
name: "capping protein regulator and myosin 1 linker 1"
location: "6p22.2"
module: 23
arm: "-"
pooled_cpm: 103.89
n_lines_expressing: 42
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CARMIL1

*capping protein regulator and myosin 1 linker 1* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +9.5, q 1e-18, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.500× (z -17.6, q 0e+00, down in 35 of 40 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.530× (z -11.4, q 8e-28, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYRIB]] (+0.64, fdr 7e-06), [[COBL]] (+0.62, fdr 1e-05), [[XPR1]] (+0.60, fdr 1e-05); moves opposite to [[KRBOX4]] (-0.60, fdr 1e-05), [[LINC01772]] (-0.55, fdr 4e-05), [[ZNF547]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLSCR4]] → it (grade B ⚠); 2 go from it, the strongest it → [[PLSCR4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +9.5 | 1e-18 | 35/40 (J82, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +6.8 | 3e-09 | 29/40 (J82, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 7e-09 | 32/41 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.6 | 5e-04 | 21/39 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.002 | 17/40 (C32, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.003 | 18/41 (J82, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.017 | 18/40 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.018 | 12/40 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.049 | 15/40 (HS-578T, hTERT-HPNE, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.055 | 15/40 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.23×** | +3.3 | 0.059 | 12/40 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.061 | 11/40 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.091 | 14/40 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.0 | 0.10 | 5/40 (C-33 A, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.500×** | -17.6 | 0e+00 | 35/40 (NCI-H2030, NCI-H23, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.530×** | -11.4 | 8e-28 | 30/40 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -8.2 | 6e-14 | 26/41 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -7.6 | 4e-12 | 33/41 (NCI-H23, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.655×** | -7.3 | 3e-11 | 26/40 (LoVo, NCI-H2030, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -7.0 | 3e-10 | 27/40 (NCI-H23, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.701×** | -6.2 | 6e-08 | 26/35 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.677×** | -6.1 | 9e-08 | 24/41 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -5.5 | 3e-06 | 22/39 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -5.4 | 4e-06 | 26/42 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **0.741×** | -5.4 | 4e-06 | 27/40 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.762×** | -4.9 | 5e-05 | 19/40 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.731×** | -4.9 | 5e-05 | 22/40 (NCI-H23, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -4.8 | 5e-05 | 21/40 (Hs 766T, A498, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.751×** | -4.8 | 7e-05 | 20/36 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -4.7 | 9e-05 | 21/40 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.844× | -4.3 | 5e-04 | 17/41 (KATO III, NCI-H23, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.770×** | -3.4 | 0.022 | 17/40 (KATO III, AN3 CA, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.884× | -3.1 | 0.043 | 9/41 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.849× | -2.9 | 0.079 | 18/40 (NCI-H23, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 171 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -31.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -14.8) |
| [[LoVo (line)]] | wt | 251 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -25.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -16.7) |
| [[NCI-H2030 (line)]] | alt | 171 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -32.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 232 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -22.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -13.6) |
| [[SW48 (line)]] | wt | 176 | 1 | 5 (3 ⚠) | [[Ponatinib (drug)]] 5 µM 2.60× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -13.0) |
| [[A-427 (line)]] | wt | 155 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -11.1) |
| [[A498 (line)]] | wt | 110 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -18.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -16.6) |
| [[C-33 A (line)]] | alt | 242 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.521× (z -9.1) |
| [[J82 (line)]] | alt | 116 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.77× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -12.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 173 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -13.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -12.0) |
| [[HS-578T (line)]] | alt | 84.2 | 2 | 2 | [[Clobetasol propionate (drug)]] 0.5 µM 3.17× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -9.8) |
| [[SW480 (line)]] | alt | 128 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.511× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 203 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -12.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 54.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -20.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.2) |
| [[HT-29 (line)]] | alt | 142 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -9.6) |
| [[KATO III (line)]] | alt | 231 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -17.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.383× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 84.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -20.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -13.5) |
| [[SW 1271 (line)]] | alt | 111 | 0 | 3 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0693× (z -11.3) |
| [[BT-474 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.129× (z -10.8) ⚠ toxic |
| [[C32 (line)]] | wt | 93.8 | 1 | 1 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 3.86× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 83.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 51.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -20.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -11.0) |
| [[A549 (line)]] | wt | 93.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -17.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0918× (z -8.9) |
| [[HCT15 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 76.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.377× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 73.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.376× (z -8.6) |
| [[A-172 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 25.1 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.4 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYRIB]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[COBL]] | +0.62 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[XPR1]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TRAK1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[RAPGEF5]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MRTFB]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SPIDR]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TBC1D1]] | +0.57 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[CERS6]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LRRC1]] | +0.56 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ZNF385B]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[CDIN1]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX4]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[LINC01772]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[ZNF547]] | -0.53 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[LRRC27]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TMEM269]] | -0.52 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[NOXRED1]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[HAVCR2]] | -0.50 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[LCA5L]] | -0.50 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[MSANTD3-TMEFF1]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[CHRNE]] | -0.50 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[GOLGA1]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[NMNAT1]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR4]] | B | PLSCR4 activity raises CARMIL1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without PLSCR4 | 0.004 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[NOS1AP]] | B | NOS1AP activity raises CARMIL1's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.72× lower at baseline in the lines without NOS1AP | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[ARHGAP8]] | B | ARHGAP8 activity raises CARMIL1's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without ARHGAP8 | 0.076 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[COBL]] | B | COBL activity raises CARMIL1's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without COBL | 0.092 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR4]] | B | CARMIL1 activity raises PLSCR4's level | lines that do not express CARMIL1 (8) vs lines expressing it (42) | 3.12× lower at baseline in the lines without CARMIL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SYNJ2, SLC22A15, MYO1D; maybe low, not absent |
| [[FGD4]] | B | CARMIL1 activity raises FGD4's level | lines that do not express CARMIL1 (8) vs lines expressing it (42) | 2.07× lower at baseline in the lines without CARMIL1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SYNJ2, SLC22A15, MYO1D; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-3.8, 36.0); signed map (-18.1, 37.4). **Vector** length 113, 32.5% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +2.8 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.3 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.9 | -17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -7.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | capping protein regulator and myosin 1 linker 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:25,279,078-25,620,530 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ501N12.1, FLJ20048, CARMIL; previously LRRC16, LRRC16A |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VZK9](https://www.uniprot.org/uniprotkb/Q5VZK9) (F-actin-uncapping protein LRRC16A):

> Cell membrane-cytoskeleton-associated protein that plays a role in the regulation of actin polymerization at the barbed end of actin filaments. Prevents F-actin heterodimeric capping protein (CP) activity at the leading edges of migrating cells, and hence generates uncapped barbed ends and enhances actin polymerization, however, seems unable to nucleate filaments. Plays a role in lamellipodial protrusion formations and cell migration.

**Summary**, from NCBI Gene [55604](https://www.ncbi.nlm.nih.gov/gene/55604):

> Involved in several processes, including actin filament network formation; plasma membrane bounded cell projection organization; and positive regulation of cellular component organization. Located in several cellular components, including cytosol; lamellipodium; and macropinosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21581) · Entrez [55604](https://www.ncbi.nlm.nih.gov/gene/55604) · UniProt [Q5VZK9](https://www.uniprot.org/uniprotkb/Q5VZK9) · Ensembl [ENSG00000079691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079691)

## Data

Gene col 1262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1262); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1262]; `tensor/DDL_lfc|DDL_z.npy` [1262]; `embed/gene_vectors.npy` [1262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1262 or target_col == 1262). Every well: [[CARMIL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARMIL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
