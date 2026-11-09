---
symbol: "ZRANB2-DT"
type: "gene"
col: 13723
ensembl_id: "ENSG00000229956"
name: "ZRANB2 divergent transcript"
location: "1p31.1"
module: 10
arm: "+"
pooled_cpm: 13.71
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 35
n_dd_up_clean: 21
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZRANB2-DT

*ZRANB2 divergent transcript* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.59× (z +5.0, q 4e-04, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.216× (z -11.7, q 1e-28, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.341× (z -8.2, q 3e-14, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP418-AS1]] (+0.83, fdr 7e-06), [[EIF1B-AS1]] (+0.78, fdr 7e-06), [[DPH6-DT]] (+0.77, fdr 7e-06); moves opposite to [[ZNRF1]] (-0.62, fdr 3e-05), [[ETHE1]] (-0.61, fdr 3e-05), [[SBK1]] (-0.59, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KIAA0825]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.0 | 4e-04 | 25/47 (A498, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.86×** | +4.7 | 6e-04 | 23/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.89×** | +4.6 | 6e-04 | 21/45 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.81×** | +4.5 | 8e-04 | 29/46 (SW480, C32, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.79×** | +4.3 | 0.002 | 28/46 (SW480, NCI-H2347, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.85×** | +4.2 | 0.002 | 24/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.76×** | +4.1 | 0.003 | 22/46 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.51×** | +4.1 | 0.004 | 22/47 (SW480, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.51×** | +4.0 | 0.004 | 26/47 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.005 | 24/47 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.005 | 23/44 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.66×** | +3.9 | 0.005 | 22/47 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.009 | 25/47 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.010 | 19/47 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **2.30×** | +3.3 | 0.035 | 13/46 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.60×** | +3.3 | 0.035 | 16/47 (SW480, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 17 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.216×** | -11.7 | 1e-28 | 43/47 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.233×** | -11.1 | 4e-26 | 40/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.276×** | -9.8 | 2e-20 | 44/47 (SNU-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.309×** | -9.0 | 5e-17 | 40/45 (NCI-H23, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.341×** | -8.2 | 3e-14 | 34/46 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.356×** | -7.6 | 4e-12 | 32/40 (HCT15, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.405×** | -6.9 | 5e-10 | 35/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.400×** | -6.7 | 1e-09 | 34/46 (RPMI-7951, SNU-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.543×** | -6.6 | 3e-09 | 30/45 (A498, C32, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.408×** | -6.6 | 3e-09 | 27/39 (LoVo, HCT15, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.433×** | -5.6 | 1e-06 | 29/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.488×** | -5.5 | 2e-06 | 24/43 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.310×** | -4.7 | 1e-04 | 30/47 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.543×** | -4.6 | 1e-04 | 26/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.548×** | -4.6 | 2e-04 | 28/47 (HCT15, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.557×** | -4.5 | 3e-04 | 31/46 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.567×** | -4.3 | 5e-04 | 25/46 (SK-MEL-2, LOX-IMVI, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.373×** | -3.9 | 0.002 | 25/44 (HS-578T, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.702×** | -3.8 | 0.004 | 22/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.601×** | -3.7 | 0.006 | 22/45 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.550×** | -3.3 | 0.027 | 17/47 (NCI-H460, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.655×** | -3.1 | 0.042 | 19/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.465×** | -3.1 | 0.048 | 17/45 (SHP-77, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.671×** | -3.0 | 0.048 | 15/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.758×** | -3.0 | 0.055 | 14/47 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.759×** | -3.0 | 0.056 | 16/47 (NCI-H1573, LOX-IMVI, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.760×** | -3.0 | 0.056 | 16/47 (C32, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 36.8 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0361× (z -13.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0912× (z -9.9) |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0594× (z -13.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0311× (z -13.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0581× (z -14.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0385× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.142× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0134× (z -16.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 38.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[HEC-1-A (line)]] | alt | 29.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0982× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0766× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.0811× (z -8.8) |
| [[HT-29 (line)]] | alt | 7.12 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0796× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0815× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 10.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.127× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0966× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 6.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0326× (z -10.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.4) ⚠ cell-cycle shift, explains ~90% of this change |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0443× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 8.57 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 8.75 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0459× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0736× (z -10.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0833× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 6.49 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0605× (z -9.3) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0712× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 5.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0453× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP418-AS1]] | +0.83 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[EIF1B-AS1]] | +0.78 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[DPH6-DT]] | +0.77 | +0.76 / +0.58 | both halves | 7e-06 | same gene group |
| [[PKN2-AS1]] | +0.77 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[MAD2L1-DT]] | +0.76 | +0.73 / +0.58 | both halves | 8e-06 | same gene group |
| [[SUCLG2-DT]] | +0.76 | +0.79 / +0.57 | both halves | 1e-05 | same gene group |
| [[MAMDC2-AS1]] | +0.73 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.73 | +0.64 / +0.65 | both halves | 7e-06 | same gene group |
| [[BDNF-AS]] | +0.73 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[GAS2]] | +0.73 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[SOX2-OT]] | +0.71 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[LINC01376]] | +0.71 | +0.70 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRF1]] | -0.62 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ETHE1]] | -0.61 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SBK1]] | -0.59 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[FCHO1]] | -0.58 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0825]] | B | KIAA0825 activity raises ZRANB2-DT's level | lines that do not express KIAA0825 (9) vs lines expressing it (41) | 1.74× lower at baseline in the lines without KIAA0825 | 0.048 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, SPART, CCDC102B; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers ZRANB2-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TNNI3K]] | C | TNNI3K activity raises ZRANB2-DT's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 2.31× lower at baseline in the lines without TNNI3K | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[MAMDC2-AS1]] | C | MAMDC2-AS1 activity raises ZRANB2-DT's level | lines that do not express MAMDC2-AS1 (3) vs lines expressing it (47) | 2.31× lower at baseline in the lines without MAMDC2-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LCA5, TEX9, TMEM178A; maybe low, not absent; its own permutation p |
| [[UBA6-DT]] | C | UBA6-DT activity raises ZRANB2-DT's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without UBA6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.7, 16.8); signed map (29.7, -9.9). **Vector** length 80.6, 20.6% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +4.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.2 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.3 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ZRANB2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p31.1 — chr1:71,081,324-71,489,976 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously ZRANB2-AS2 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43595) · Entrez [100852410](https://www.ncbi.nlm.nih.gov/gene/100852410) · Ensembl [ENSG00000229956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229956)

## Data

Gene col 13723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13723); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13723]; `tensor/DDL_lfc|DDL_z.npy` [13723]; `embed/gene_vectors.npy` [13723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13723 or target_col == 13723). Every well: [[ZRANB2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZRANB2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
