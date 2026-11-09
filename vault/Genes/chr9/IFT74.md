---
symbol: "IFT74"
type: "gene"
col: 1772
ensembl_id: "ENSG00000096872"
name: "intraflagellar transport 74"
location: "9p21.2"
module: 28
arm: "+"
pooled_cpm: 44.32
n_lines_expressing: 47
n_dd_up: 28
n_dd_down: 22
n_dd_up_clean: 26
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# IFT74

*intraflagellar transport 74* — 9p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +20.0, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.389× (z -21.6, q 0e+00, down in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.418× (z -19.9, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COQ5]] (+0.73, fdr 1e-05), [[DZIP3]] (+0.68, fdr 2e-05), [[ZNF181]] (+0.68, fdr 4e-05); moves opposite to [[LPCAT4]] (-0.63, fdr 3e-05), [[ARHGAP8]] (-0.60, fdr 1e-05), [[TRABD]] (-0.60, fdr 8e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TP53]] → it (grade C ⚠); 8 go from it, the strongest it → cells under [[Tomivosertib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +20.0 | 0e+00 | 38/45 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +13.9 | 1e-41 | 38/45 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +10.7 | 1e-24 | 32/45 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.7 | 2e-24 | 29/45 (MIA PaCa-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +9.6 | 1e-19 | 30/45 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +6.5 | 7e-09 | 22/45 (RKO, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.4 | 9e-09 | 25/45 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +6.4 | 1e-08 | 27/45 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +6.0 | 1e-07 | 24/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +5.9 | 2e-07 | 19/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.20×** | +5.8 | 4e-07 | 20/45 (SW480, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +5.5 | 2e-06 | 19/45 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.4 | 4e-06 | 20/45 (KATO III, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.3 | 5e-06 | 19/45 (Panc 03.27, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +4.9 | 4e-05 | 20/45 (HS-578T, COLO 205, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.21×** | +4.4 | 4e-04 | 13/45 (NCI-H2030, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.389×** | -21.6 | 0e+00 | 44/45 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.418×** | -19.9 | 0e+00 | 44/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.451×** | -18.2 | 0e+00 | 45/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.478×** | -16.9 | 0e+00 | 44/45 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.594×** | -11.5 | 2e-28 | 35/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.613×** | -11.2 | 5e-27 | 35/45 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.509×** | -8.1 | 6e-14 | 28/45 (SHP-77, H4, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.725×** | -7.3 | 2e-11 | 28/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -7.1 | 6e-11 | 26/45 (A498, SNU-423, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.767×** | -6.1 | 7e-08 | 26/45 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.768×** | -6.0 | 9e-08 | 23/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.831×** | -6.0 | 1e-07 | 20/45 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.618×** | -5.8 | 4e-07 | 20/45 (A498, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.779×** | -5.7 | 5e-07 | 24/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.730×** | -5.1 | 1e-05 | 18/45 (NCI-H460, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.815×** | -4.7 | 1e-04 | 21/45 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.696×** | -4.3 | 5e-04 | 17/45 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.001 | 16/45 (AN3 CA, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.835× | -3.9 | 0.003 | 16/45 (A-427, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 51.9 | 1 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.280× (z -15.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -14.6) |
| [[SW480 (line)]] | alt | 52.7 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.187× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -20.9) |
| [[A498 (line)]] | wt | 173 | 0 | 6 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.298× (z -13.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -11.7) |
| [[HOP62 (line)]] | alt | 43.8 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.6) | [[Digitoxin (drug)]] 0.5 µM 0.262× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 56.5 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -11.9) |
| [[PANC-1 (line)]] | alt | 27.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.270× (z -14.2) |
| [[SNU-423 (line)]] | alt | 57.2 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -11.6) |
| [[A-427 (line)]] | wt | 39.5 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.302× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.388× (z -9.4) |
| [[HS-578T (line)]] | alt | 48.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -12.8) |
| [[LoVo (line)]] | wt | 32.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.340× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 62.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.0668× (z -29.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 34.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.367× (z -9.9) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 49.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.290× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.355× (z -9.1) |
| [[J82 (line)]] | alt | 39.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 22.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.6) | [[Lonafarnib (drug)]] 5 µM 0.0894× (z -9.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 38.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +15.3) | [[Digitoxin (drug)]] 5 µM 0.315× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 50.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +14.2) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 43.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.205× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 55.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 71.8 | 0 | 2 (1 ⚠) | — | [[Hesperidin (drug)]] 5 µM 0.129× (z -11.7) |
| [[C-33 A (line)]] | alt | 76.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.253× (z -12.9) |
| [[HCT15 (line)]] | alt | 45.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.198× (z -11.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 30.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 35.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 18.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -10.9) |
| [[A-172 (line)]] | wt | 45.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -10.1) |
| [[KATO III (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 77.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0909× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 58.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -11.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 41.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.317× (z -8.7) |
| [[SW48 (line)]] | wt | 38.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 66.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ5]] | +0.73 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[DZIP3]] | +0.68 | +0.81 / +0.47 | both halves | 2e-05 |  |
| [[ZNF181]] | +0.68 | +0.79 / +0.42 | both halves | 4e-05 |  |
| [[SEPSECS]] | +0.67 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[SUPT20H]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ANKRD26]] | +0.67 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[PMPCB]] | +0.67 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[RAD52]] | +0.66 | +0.82 / +0.37 | both halves | 8e-05 |  |
| [[PHYH]] | +0.66 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[CCDC25]] | +0.66 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[FBXO8]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.66 | +0.75 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT4]] | -0.63 | -0.74 / -0.45 | both halves | 3e-05 |  |
| [[ARHGAP8]] | -0.60 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[TRABD]] | -0.60 | -0.71 / -0.37 | both halves | 8e-05 |  |
| [[TPST2]] | -0.60 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.59 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[USB1]] | -0.59 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[CORO7]] | -0.59 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[LMBR1]] | -0.58 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[KYAT1]] | -0.58 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[ANKS6]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TBC1D24]] | -0.57 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[CPSF4]] | -0.57 | -0.60 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | C | TP53 activity raises IFT74's level | lines that do not express TP53 (3) vs lines expressing it (47) | 3.00× lower at baseline in the lines without TP53 | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF483, AGK, MCM2; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tomivosertib (drug)]] 5 µM | C | IFT74 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express IFT74 (3) vs lines expressing it (45) | the lines without IFT74: 0.69× the cells of the other lines | 0.007 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| cells under [[Neratinib (maleate) (drug)]] 5 µM | C | IFT74 activity raises the cells' numbers under Neratinib (maleate) 5 µM (protects the cells) | lines that do not express IFT74 (3) vs lines expressing it (45) | the lines without IFT74: 0.81× the cells of the other lines | 0.017 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| [[C17orf75]] | C | IFT74 activity raises C17orf75's level | lines that do not express IFT74 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without IFT74 | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| cells under [[Trifluridine (drug)]] 0.5 µM | C | IFT74 activity lowers the cells' numbers under Trifluridine 0.5 µM (makes them more sensitive) | lines that do not express IFT74 (3) vs lines expressing it (45) | the lines without IFT74: 1.34× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| [[TRMT1L]] | C | IFT74 activity raises TRMT1L's level | lines that do not express IFT74 (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without IFT74 | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| cells under [[Anethole trithione (drug)]] 5 µM | C | IFT74 activity raises the cells' numbers under Anethole trithione 5 µM (protects the cells) | lines that do not express IFT74 (3) vs lines expressing it (45) | the lines without IFT74: 0.86× the cells of the other lines | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| [[TRAFD1]] | C | IFT74 activity lowers TRAFD1's level | lines that do not express IFT74 (3) vs lines expressing it (47) | 1.65× higher at baseline in the lines without IFT74 | 0.091 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| cells under [[EX229 (drug)]] 0.5 µM | C | IFT74 activity raises the cells' numbers under EX229 0.5 µM (protects the cells) | lines that do not express IFT74 (3) vs lines expressing it (45) | the lines without IFT74: 0.71× the cells of the other lines | 0.096 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.9, 6.0); signed map (8.1, -24.3). **Vector** length 105, 27.7% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.4 | +13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +20.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +5.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.4 | -7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -21.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -11.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.8 | -18.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 74 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.2 — chr9:26,947,039-27,066,134 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CMG1, CMG-1, FLJ22621; previously CCDC2 |
| Gene groups (HGNC) | IFT-B1 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LB3](https://www.uniprot.org/uniprotkb/Q96LB3) (Intraflagellar transport protein 74 homolog):

> Component of the intraflagellar transport (IFT) complex B: together with IFT81, forms a tubulin-binding module that specifically mediates transport of tubulin within the cilium. Binds beta-tubulin via its basic region. Required for ciliogenesis. Essential for flagellogenesis during spermatogenesis.

**Summary**, from NCBI Gene [80173](https://www.ncbi.nlm.nih.gov/gene/80173):

> This gene encodes a core intraflagellar transport (IFT) protein which belongs to a multi-protein complex involved in the transport of ciliary proteins along axonemal microtubules. IFT proteins are found at the base of the cilium as well as inside the cilium, where they assemble into long arrays between the ciliary base and tip. This protein, together with intraflagellar transport protein 81, binds and transports tubulin within cilia and is required for ciliogenesis. Naturally occurring …

**Accessions** — [HGNC:21424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21424) · Entrez [80173](https://www.ncbi.nlm.nih.gov/gene/80173) · UniProt [Q96LB3](https://www.uniprot.org/uniprotkb/Q96LB3) · Ensembl [ENSG00000096872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096872)

## Data

Gene col 1772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1772); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1772]; `tensor/DDL_lfc|DDL_z.npy` [1772]; `embed/gene_vectors.npy` [1772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1772 or target_col == 1772). Every well: [[IFT74 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT74.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
