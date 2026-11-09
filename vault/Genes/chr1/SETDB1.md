---
symbol: "SETDB1"
type: "gene"
col: 6730
ensembl_id: "ENSG00000143379"
name: "SET domain bifurcated histone lysine methyltransferase 1"
location: "1q21.3"
module: 114
arm: "+"
pooled_cpm: 54.4
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# SETDB1

*SET domain bifurcated histone lysine methyltransferase 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.21× (z +5.8, q 3e-06, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.487× (z -21.7, q 0e+00, down in 42 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.695× (z -15.5, q 0e+00, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COIL]] (+0.76, fdr 7e-06), [[ECSIT]] (+0.73, fdr 7e-06), [[ZC3HC1]] (+0.72, fdr 7e-06); moves opposite to [[DIAPH1]] (-0.61, fdr 1e-05), [[RALB]] (-0.59, fdr 1e-05), [[EPB41L2]] (-0.59, fdr 7e-06).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +5.8 | 3e-06 | 21/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 5e-06 | 22/47 (A-172, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.34×** | +4.6 | 8e-04 | 21/49 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +4.4 | 0.001 | 18/47 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.15× | +4.3 | 0.002 | 13/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.15× | +4.0 | 0.005 | 10/48 (NCI-H23, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.9 | 0.008 | 17/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.047 | 3/48 (CFPAC-1, HT-29, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.1 | 0.10 | 8/48 (SNU-1, NCI-H23, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.22× | +3.1 | 0.10 | 8/47 (SW480, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.11× | +3.1 | 0.10 | 2/49 (CFPAC-1, AsPC-1) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.487×** | -21.7 | 0e+00 | 42/48 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.485×** | -21.1 | 0e+00 | 34/44 (SHP-77, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.556×** | -17.7 | 0e+00 | 44/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.564×** | -17.3 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.558×** | -16.3 | 0e+00 | 32/44 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -15.5 | 0e+00 | 38/49 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.640×** | -13.5 | 2e-39 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.655×** | -12.8 | 1e-35 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.726×** | -9.7 | 3e-20 | 29/48 (NCI-H460, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.768×** | -7.7 | 1e-12 | 28/49 (A-172, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.777×** | -7.6 | 1e-12 | 30/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.775×** | -7.4 | 6e-12 | 26/47 (A-172, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.706×** | -5.5 | 2e-06 | 20/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.828×** | -5.5 | 2e-06 | 23/47 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.867× | -4.3 | 7e-04 | 15/48 (NCI-H460, A549, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.920× | -3.5 | 0.015 | 10/48 (NCI-H460, SW1417, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.890× | -3.4 | 0.022 | 8/47 (NCI-H460, NCI-H2347, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.926× | -3.3 | 0.031 | 13/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.053 | 13/48 (hTERT-HPNE, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.3 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -20.5) |
| [[A-172 (line)]] | wt | 83.7 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -21.1) |
| [[PANC-1 (line)]] | alt | 72.4 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.545× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 55.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 62.0 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 67.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 53.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.555× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 92.2 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -8.7) |
| [[SNU-1 (line)]] | wt | 69.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.5) |
| [[A549 (line)]] | wt | 52.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -8.7) |
| [[C32 (line)]] | wt | 38.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.2) |
| [[A-427 (line)]] | wt | 56.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 49.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -12.1) |
| [[C-33 A (line)]] | alt | 58.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[CHP-212 (line)]] | wt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 54.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.431× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 37.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -12.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 52.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 61.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 49.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 98.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0980× (z -27.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 42.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0894× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 33.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.2) |
| [[LoVo (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0916× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -17.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COIL]] | +0.76 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[ECSIT]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.70 | +0.70 / +0.75 | both halves | 7e-06 | STRING 432 |
| [[TEFM]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[RBM5]] | +0.69 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ZCCHC10]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ZNF573]] | +0.69 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ZNF226]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[POLL]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[MAU2]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | STRING 489 |
| [[SRSF11]] ⚠ | +0.68 | +0.60 / +0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ALKBH4]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.61 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[RALB]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.59 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[YWHAZ]] | -0.59 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[G6PD]] | -0.58 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[AP2M1]] | -0.57 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[TMED7]] | -0.57 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[IQGAP1]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ACLY]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SETDB1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.9, 7.2); signed map (-6.5, -14.4). **Vector** length 94.6, 21.7% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.3 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.6 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +5.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.6 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.5 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | -3.7 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -3.0 | -21.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.9 | -16.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.8 | -7.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -5.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SET domain bifurcated histone lysine methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,926,263-150,964,744 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KG1T, KIAA0067, ESET, KMT1E, TDRD21 |
| Gene groups (HGNC) | Histone lysine methyltransferases; Tudor domain containing; Methyl-CpG binding domain containing; SET domain containing |
| Reactome | 7 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; PKMTs methylate histone lysines; Regulation of endogenous retroelements by KRAB-ZFP proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15047](https://www.uniprot.org/uniprotkb/Q15047) (Histone-lysine N-methyltransferase SETDB1):

> Histone methyltransferase that specifically trimethylates 'Lys-9' of histone H3 (H3K9me3). H3 'Lys-9' trimethylation represents a specific tag for epigenetic transcriptional repression by recruiting HP1 (CBX1, CBX3 and/or CBX5) proteins to methylated histones. Mainly functions in euchromatin regions, thereby playing a central role in the silencing of euchromatic genes. H3 'Lys-9' trimethylation is coordinated with DNA methylation. Forms a complex with MBD1 and ATF7IP that represses …

**Summary**, from NCBI Gene [9869](https://www.ncbi.nlm.nih.gov/gene/9869):

> This gene encodes a histone methyltransferase which regulates histone methylation, gene silencing, and transcriptional repression. This gene has been identified as a target for treatment in Huntington Disease, given that gene silencing and transcription dysfunction likely play a role in the disease pathogenesis. Alternatively spliced transcript variants of this gene have been described.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:10761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10761) · Entrez [9869](https://www.ncbi.nlm.nih.gov/gene/9869) · UniProt [Q15047](https://www.uniprot.org/uniprotkb/Q15047) · Ensembl [ENSG00000143379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143379)

## Data

Gene col 6730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6730); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6730]; `tensor/DDL_lfc|DDL_z.npy` [6730]; `embed/gene_vectors.npy` [6730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6730 or target_col == 6730). Every well: [[SETDB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETDB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
