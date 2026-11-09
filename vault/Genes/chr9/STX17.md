---
symbol: "STX17"
type: "gene"
col: 5927
ensembl_id: "ENSG00000136874"
name: "syntaxin 17"
location: "9q31.1"
module: 32
arm: "+"
pooled_cpm: 54.22
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# STX17

*syntaxin 17* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.40× (z +6.0, q 9e-07, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.354× (z -18.3, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.459× (z -13.8, q 1e-40, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMI]] (+0.72, fdr 7e-06), [[DTX3L]] (+0.71, fdr 7e-06), [[DDX60]] (+0.69, fdr 7e-06); moves opposite to [[RAB43]] (-0.65, fdr 9e-06), [[SDHAP4-1]] (-0.57, fdr 1e-05), [[ANKRD13D]] (-0.57, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DDX60L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.0 | 9e-07 | 29/48 (A-172, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +5.2 | 7e-05 | 31/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.003 | 27/48 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 0.003 | 26/47 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.012 | 20/48 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.012 | 19/48 (A-172, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.23×** | +3.8 | 0.012 | 22/49 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.012 | 24/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.025 | 18/48 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.027 | 12/48 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.041 | 20/48 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.054 | 17/49 (KATO III, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.069 | 17/47 (SW 900, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.069 | 15/48 (SW480, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +3.1 | 0.081 | 14/48 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.081 | 16/48 (J82, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.354×** | -18.3 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.459×** | -13.8 | 1e-40 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.485×** | -12.8 | 4e-35 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.502×** | -12.2 | 7e-32 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.319×** | -10.6 | 4e-24 | 44/49 (SK-MEL-2, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.341×** | -9.9 | 3e-21 | 40/48 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -9.0 | 1e-17 | 38/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -9.0 | 1e-17 | 35/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -6.9 | 3e-10 | 41/48 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.769×** | -6.5 | 4e-09 | 30/48 (COLO 205, LoVo, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.719×** | -5.8 | 3e-07 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.821×** | -4.9 | 5e-05 | 26/49 (CFPAC-1, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.772×** | -4.5 | 2e-04 | 25/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.779×** | -4.2 | 0.001 | 25/48 (SNU-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.792×** | -4.1 | 0.002 | 24/48 (Panc 03.27, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -4.1 | 0.002 | 24/48 (LoVo, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.814×** | -3.6 | 0.009 | 21/47 (MIA PaCa-2, H4, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.034 | 15/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.712×** | -3.1 | 0.043 | 17/48 (HT-29, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 70.4 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -22.1) |
| [[LoVo (line)]] | wt | 68.9 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 52.6 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.256× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 56.0 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.400× (z -8.9) |
| [[COLO 205 (line)]] | alt | 121 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -10.1) |
| [[PANC-1 (line)]] | alt | 31.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.345× (z -12.3) |
| [[SHP-77 (line)]] | alt | 44.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0725× (z -12.5) |
| [[SNU-423 (line)]] | alt | 60.9 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -10.0) |
| [[A-172 (line)]] | wt | 101 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -13.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.148× (z -11.5) |
| [[A549 (line)]] | wt | 77.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 45.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -10.7) |
| [[LS 180 (line)]] | wt | 53.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 80.5 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.174× (z -9.6) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.214× (z -8.5) |
| [[SW1417 (line)]] | alt | 53.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.271× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -10.3) |
| [[H4 (line)]] | wt | 53.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -10.1) |
| [[HCT15 (line)]] | alt | 80.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.353× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.394× (z -8.5) |
| [[Hs 766T (line)]] | wt | 47.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.362× (z -8.9) |
| [[HS-578T (line)]] | alt | 32.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.302× (z -9.7) |
| [[HT-29 (line)]] | alt | 54.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.314× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.191× (z -9.1) |
| [[KATO III (line)]] | alt | 69.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.361× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.249× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 74.8 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.332× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 43.8 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0881× (z -10.4) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 63.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 57.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~2% of this change |
| [[HOP62 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -12.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.219× (z -10.5) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0430× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 56.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.295× (z -9.4) |
| [[SNU-1 (line)]] | wt | 50.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMI]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[DTX3L]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DDX60]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ADAR]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[RBM43]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[PARP14]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TIGD2]] | +0.64 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[IFIH1]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[VPS13C]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SP100]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PSMB8]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TRIM21]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB43]] | -0.65 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[SDHAP4-1]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[ANKRD13D]] | -0.57 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CSNK1G2]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ZNF668]] | -0.57 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[CD81]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[HYAL1]] | -0.56 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[RNF139-DT]] | -0.55 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[ST6GALNAC6-1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RBM14-RBM4]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX60L]] | B | DDX60L activity raises STX17's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 1.20× lower at baseline in the lines without DDX60L | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers STX17's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.2, 54.6); signed map (62.4, 33.0). **Vector** length 87.4, 23.8% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.52 to 23); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.52 to 21); *IFIT antiviral response* (reactome, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.9 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.8 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -6.2 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -6.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.3 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.0 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.8 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:99,906,654-99,974,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20651 |
| Gene groups (HGNC) | Syntaxins |
| Reactome | 6 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P56962](https://www.uniprot.org/uniprotkb/P56962) (Syntaxin-17):

> SNAREs, soluble N-ethylmaleimide-sensitive factor-attachment protein receptors, are essential proteins for fusion of cellular membranes. SNAREs localized on opposing membranes assemble to form a trans-SNARE complex, an extended, parallel four alpha-helical bundle that drives membrane fusion. STX17 is a SNARE of the autophagosome involved in autophagy through the direct control of autophagosome membrane fusion with the lysosome membrane. May also play a role in the early secretory pathway where …

**Summary**, from NCBI Gene [55014](https://www.ncbi.nlm.nih.gov/gene/55014):

> Enables SNAP receptor activity; SNARE binding activity; and protein phosphatase binding activity. Involved in several processes, including endoplasmic reticulum to Golgi vesicle-mediated transport; endoplasmic reticulum-Golgi intermediate compartment organization; and macroautophagy. Acts upstream of or within protein localization to phagophore assembly site. Located in several cellular components, including endoplasmic reticulum-Golgi intermediate compartment; mitochondria-associated …

**Accessions** — [HGNC:11432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11432) · Entrez [55014](https://www.ncbi.nlm.nih.gov/gene/55014) · UniProt [P56962](https://www.uniprot.org/uniprotkb/P56962) · Ensembl [ENSG00000136874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136874)

## Data

Gene col 5927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5927); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5927]; `tensor/DDL_lfc|DDL_z.npy` [5927]; `embed/gene_vectors.npy` [5927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5927 or target_col == 5927). Every well: [[STX17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
