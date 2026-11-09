---
symbol: "TACC2"
type: "gene"
col: 6136
ensembl_id: "ENSG00000138162"
name: "transforming acidic coiled-coil containing protein 2"
location: "10q26.13"
module: 105
arm: "+"
pooled_cpm: 76.91
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# TACC2

*transforming acidic coiled-coil containing protein 2* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +10.9, q 1e-24, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.506× (z -14.0, q 5e-42, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW10B]] (+0.53, fdr 3e-05), [[GNA14]] (+0.53, fdr 4e-05), [[GNGT1]] (+0.52, fdr 6e-05); moves opposite to [[USP37]] (-0.57, fdr 2e-05), [[FAM210A]] (-0.53, fdr 5e-05), [[TCAF2]] (-0.52, fdr 6e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[JAKMIP3]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Belinostat (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +10.9 | 1e-24 | 30/45 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +8.5 | 8e-15 | 28/44 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +6.6 | 8e-09 | 29/45 (C32, SW480, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 2e-06 | 24/45 (C32, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +4.6 | 4e-04 | 15/44 (SHP-77, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.006 | 18/44 (C32, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.006 | 19/45 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.9 | 0.006 | 19/44 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.006 | 18/45 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.006 | 10/45 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 19/45 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.1 | 0.078 | 15/45 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.099 | 11/45 (A498, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.506×** | -14.0 | 5e-42 | 36/45 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.535×** | -12.9 | 2e-35 | 36/45 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.547×** | -12.5 | 3e-33 | 33/45 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.639×** | -8.9 | 9e-17 | 24/39 (HCT15, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.792×** | -4.8 | 2e-04 | 18/44 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.792×** | -4.6 | 4e-04 | 21/44 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.802×** | -4.5 | 5e-04 | 20/44 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.809×** | -4.4 | 9e-04 | 21/45 (LS 180, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.811×** | -4.0 | 0.004 | 18/41 (SW48, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.819×** | -4.0 | 0.004 | 19/47 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.825×** | -4.0 | 0.004 | 20/44 (LoVo, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.835× | -3.7 | 0.010 | 16/45 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.881× | -3.7 | 0.010 | 7/46 (NCI-H1573, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.826×** | -3.4 | 0.024 | 20/45 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Amsacrine (drug)]] 5 µM |  | 0.889× | -3.4 | 0.024 | 8/45 (HOP62, RKO, …) | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | 0.846× | -3.3 | 0.030 | 16/44 (SW480, SW48, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.895× | -3.2 | 0.039 | 6/46 (LOX-IMVI, Hs 766T, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.848× | -2.9 | 0.090 | 11/44 (AN3 CA, C32, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.821×** | -2.9 | 0.095 | 4/45 (AsPC-1, SHP-77, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 179 | 18 | 10 (5 ⚠) | [[Budesonide (drug)]] 5 µM 3.18× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -17.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.331× (z -15.6) |
| [[LoVo (line)]] | wt | 174 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -17.5) |
| [[NCI-H1573 (line)]] | alt | 68.5 | 7 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.32× (z +9.4) ⚠ toxic · without an alert: [[Cobimetinib (drug)]] 5 µM 3.22× (z +9.2) | — |
| [[A-427 (line)]] | wt | 61.6 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.339× (z -10.8) |
| [[LS 180 (line)]] | wt | 205 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 103 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.506× (z -9.8) |
| [[PANC-1 (line)]] | alt | 158 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.440× (z -10.7) |
| [[HT-29 (line)]] | alt | 158 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.281× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 64.6 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.330× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.423× (z -10.2) |
| [[C-33 A (line)]] | alt | 58.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -11.3) |
| [[KATO III (line)]] | alt | 98.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -10.1) |
| [[RKO (line)]] | wt | 97.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -9.4) |
| [[SW48 (line)]] | wt | 62.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.221× (z -10.6) |
| [[SW480 (line)]] | alt | 57.9 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.62× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[AN3 CA (line)]] | alt | 112 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -11.6) |
| [[HS-578T (line)]] | alt | 36.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.359× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 25.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +15.5) | — |
| [[SNU-1 (line)]] | wt | 280 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 56.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -9.5) |
| [[HCT15 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.1000× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 84.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[J82 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.0) | — |
| [[NCI-H596 (line)]] | alt | 78.5 | 1 | 0 | [[Oxaprozin (drug)]] 5 µM 3.30× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 72.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[SW1417 (line)]] | alt | 81.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW10B]] | +0.53 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[GNA14]] | +0.53 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[GNGT1]] | +0.52 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[SMG1-DT]] | +0.52 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[SLC25A13]] | +0.51 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[NFE2L2]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[DNAJB12]] | +0.50 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[HTR1D]] | +0.50 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[PSMD11]] | +0.49 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[MYO16]] | +0.49 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[INO80]] | +0.49 | +0.42 / +0.38 | both halves | 7e-05 |  |
| [[USP7]] | +0.49 | +0.44 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP37]] | -0.57 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[FAM210A]] | -0.53 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[TCAF2]] | -0.52 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[RAB8B]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NUP58]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ANKRD37]] | -0.50 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[SFXN1]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[AP3S1]] | -0.49 | -0.51 / -0.43 | both halves | 4e-05 |  |
| [[INSIG2]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[POM121C]] | -0.49 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[GUK1]] | -0.49 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[WDR45B]] | -0.49 | -0.53 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAKMIP3]] | B | JAKMIP3 activity raises TACC2's level | lines that do not express JAKMIP3 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without JAKMIP3 | 0.037 | ⚠ within organs, on part of the lines; also absent: RHOU, ABCG1, CASZ1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belinostat (drug)]] 5 µM | C | TACC2 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express TACC2 (3) vs lines expressing it (45) | the lines without TACC2: 0.59× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NME3, OSR2, H1-0; maybe low, not absent |
| cells under [[Panobinostat (drug)]] 5 µM | C | TACC2 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express TACC2 (3) vs lines expressing it (45) | the lines without TACC2: 0.58× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: NME3, OSR2, H1-0; maybe low, not absent |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | C | TACC2 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express TACC2 (3) vs lines expressing it (45) | the lines without TACC2: 0.43× the cells of the other lines | 0.076 | ⚠ few lines (3 vs 47); across organs; also absent: NME3, OSR2, H1-0; maybe low, not absent |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction -0.543). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, -20.1); signed map (51.2, -6.5). **Vector** length 116, 30.7% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +10.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.6 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.5 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.4 | +6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.6 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -14.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -12.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -12.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.0 | -3.0 |
|  | [[Ciclopirox (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transforming acidic coiled-coil containing protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:121,989,163-122,254,545 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AZU-1, ECTACC |
| Gene groups (HGNC) | TACC family |
| Matched by | ensembl_id |

**Function**, from UniProt [O95359](https://www.uniprot.org/uniprotkb/O95359) (Transforming acidic coiled-coil-containing protein 2):

> Plays a role in the microtubule-dependent coupling of the nucleus and the centrosome. Involved in the processes that regulate centrosome-mediated interkinetic nuclear migration (INM) of neural progenitors (By similarity). May play a role in organizing centrosomal microtubules. May act as a tumor suppressor protein. May represent a tumor progression marker.

**Summary**, from NCBI Gene [10579](https://www.ncbi.nlm.nih.gov/gene/10579):

> Transforming acidic coiled-coil proteins are a conserved family of centrosome- and microtubule-interacting proteins that are implicated in cancer. This gene encodes a protein that concentrates at centrosomes throughout the cell cycle. This gene lies within a chromosomal region associated with tumorigenesis. Expression of this gene is induced by erythropoietin and is thought to affect the progression of breast tumors. Several transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:11523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11523) · Entrez [10579](https://www.ncbi.nlm.nih.gov/gene/10579) · UniProt [O95359](https://www.uniprot.org/uniprotkb/O95359) · Ensembl [ENSG00000138162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138162)

## Data

Gene col 6136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6136); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6136]; `tensor/DDL_lfc|DDL_z.npy` [6136]; `embed/gene_vectors.npy` [6136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6136 or target_col == 6136). Every well: [[TACC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TACC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
